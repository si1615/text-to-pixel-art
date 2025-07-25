# 🎨 Pixel Art Code Generator (Python + Tkinter)

A lightweight Python app that turns custom color-coded strings into pixel art with a live preview and save feature. Ideal for learning image generation, creative expression, or designing your own pixel format.

<img width="240" height="240" alt="pixel" src="https://github.com/user-attachments/assets/0992a011-f55f-43dd-83a5-068796e198df" />


---

## ✨ Features

- ✅ Type pixel codes in a simple `{widthxheight}` format
- 🧠 Uses digits (`0`–`9`) and color codes for easy pixel control
- 🎨 Blended and hex colors supported (e.g. `0-1`, `[FF00FF]`)
- 🔁 **Live preview** as you type
- 💾 Save your pixel art as PNG with one click
- 🐍 Written in pure Python with Tkinter + Pillow

---

## 🧾 Format Overview

- Input starts with dimensions like `{8x8}`
- Followed by color codes:
  - `0–9`: mapped to basic colors
  - `0-1`: blend two color codes
  - `[RRGGBB]`: custom hex color

Example:
{5x3}01234
12345
23456

yaml
Copy
Edit

---

## 🎨 Color Code Legend

| Code | Color     |
|------|-----------|
| 0    | Black     |
| 1    | White     |
| 2    | Red       |
| 3    | Orange    |
| 4    | Yellow    |
| 5    | Green     |
| 6    | Blue      |
| 7    | Purple    |
| 8    | Pink      |
| 9    | Teal      |
| 0-1  | Gray (blend) |
| [RRGGBB] | Custom hex |

---

## 🐱 Example (bad) Cat (8x8)

{8x8}00001100
01112210
01223310
01233310
01222210
00111000
00000000
00000000



---

## 🚀 How to Run

1. Make sure you have Python 3 installed
2. Install Pillow:
pip install pillow
Run the app:
python pixel_art_app.py
