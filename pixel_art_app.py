import re
import threading
from tkinter import Tk, Text, Button, Label, END, messagebox, filedialog
from PIL import Image, ImageTk

# Color map for 0-9
basic_colors = {
    "0": (0, 0, 0),        # Black
    "1": (255, 255, 255),  # White
    "2": (255, 0, 0),      # Red
    "3": (255, 128, 0),    # Orange
    "4": (255, 255, 0),    # Yellow
    "5": (0, 255, 0),      # Green
    "6": (0, 0, 255),      # Blue
    "7": (128, 0, 128),    # Purple
    "8": (255, 105, 180),  # Pink
    "9": (0, 255, 255),    # Teal
}

def blend(c1, c2):
    return tuple((a + b) // 2 for a, b in zip(c1, c2))

def parse_color(token):
    if token in basic_colors:
        return basic_colors[token]
    elif "-" in token:
        parts = token.split("-")
        if all(p in basic_colors for p in parts):
            color = basic_colors[parts[0]]
            for p in parts[1:]:
                color = blend(color, basic_colors[p])
            return color
    elif token.startswith("[") and token.endswith("]"):
        hex_val = token[1:-1]
        if len(hex_val) == 6:
            try:
                r = int(hex_val[0:2], 16)
                g = int(hex_val[2:4], 16)
                b = int(hex_val[4:6], 16)
                return (r, g, b)
            except ValueError:
                return (0, 0, 0)
    return (0, 0, 0)  # Fallback to black

def make_pixel_art(code, scale=30):
    size_match = re.match(r"\{(\d+)x(\d+)\}", code)
    if not size_match:
        raise ValueError("Invalid format: start with {widthxheight}")
    width, height = map(int, size_match.groups())
    data = code[size_match.end():]

    tokens = []
    i = 0
    while i < len(data):
        if data[i] == "[":
            end = data.find("]", i) + 1
            if end == 0:
                raise ValueError("Invalid hex color format")
            tokens.append(data[i:end])
            i = end
        elif i + 2 < len(data) and data[i+1] == "-":
            tokens.append(data[i:i+3])
            i += 3
        else:
            tokens.append(data[i])
            i += 1

    if len(tokens) < width * height:
        tokens.extend(["0"] * (width * height - len(tokens)))  # fill missing with black

    img = Image.new("RGB", (width, height))
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            idx = y * width + x
            pixels[x, y] = parse_color(tokens[idx])

    img = img.resize((width*scale, height*scale), Image.NEAREST)
    return img

# GUI setup
class PixelArtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Generator with Live Preview & Save")

        self.label = Label(root, text="Enter pixel art code:\nFormat: {widthxheight}pixels\nExample: {5x2}0123456789")
        self.label.pack(pady=5)

        self.text_input = Text(root, height=5, width=40)
        self.text_input.pack()
        self.text_input.bind("<<Modified>>", self.on_text_change)

        self.generate_btn = Button(root, text="Save Pixel Art", command=self.save_image)
        self.generate_btn.pack(pady=10)

        self.preview_label = Label(root)
        self.preview_label.pack()

        self.current_img = None
        self.update_after_id = None

    def on_text_change(self, event=None):
        # Reset the modified flag (so event triggers again next time)
        self.text_input.edit_modified(False)
        # Use after() to delay update for smoother typing experience
        if self.update_after_id:
            self.root.after_cancel(self.update_after_id)
        self.update_after_id = self.root.after(500, self.update_preview)  # 500 ms delay

    def update_preview(self):
        code = self.text_input.get("1.0", END).strip()
        if not code:
            self.preview_label.config(image='', text='No input')
            self.current_img = None
            return
        try:
            img = make_pixel_art(code)
            self.current_img = img
            img_tk = ImageTk.PhotoImage(img)
            self.preview_label.config(image=img_tk, text='')
            self.preview_label.image = img_tk  # keep reference
        except Exception as e:
            self.preview_label.config(text=f"Error: {e}", image='')
            self.current_img = None

    def save_image(self):
        if self.current_img is None:
            messagebox.showwarning("No image", "No valid pixel art to save!")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save Pixel Art as PNG"
        )
        if file_path:
            try:
                self.current_img.save(file_path)
                messagebox.showinfo("Saved", f"Image saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error saving file", str(e))


if __name__ == "__main__":
    root = Tk()
    app = PixelArtApp(root)
    root.mainloop()
