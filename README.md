# text-to-pixel-art
🎨 Pixel Art Code Generator (Python + Tkinter)
A lightweight Python app that turns custom color-coded strings into pixel art images using a live preview and save feature. Ideal for learning about image processing, creative coding, or building your own pixel art language.

✨ Features
✅ Custom pixel input format like {widthxheight}012345...

🎨 Supports blended colors (e.g. 0-1) and hex codes (e.g. [FF00FF])

⚡ Live preview as you type

💾 Save final output to PNG with one click

🧠 Color codes based on digits for easy use

🎨 Color Code Legend
Code	Color
0	Black
1	White
2	Red
3	Orange
4	Yellow
5	Green
6	Blue
7	Purple
8	Pink
9	Teal
0-1	Gray (blend)
[RRGGBB]	Custom hex color

🧪 Example Input
Copy
Edit
{5x3}01234\
12345\
23456
Creates a 5×3 pixel art image with digits mapped to their colors.

🖥️ How to Run
Make sure you have Python 3 and Pillow installed:

bash
Copy
Edit
pip install pillow
Run the app:

bash
Copy
Edit
python pixel_art_app.py
Type your art string into the textbox and see live preview instantly!

🗂️ File Structure
bash
Copy
Edit
pixel_art_app.py  # Main program
README.md         # This file
🐱 Want Examples?
Try this simple cat face:

Copy
Edit
{8x8}00001100\
01112210\
01223310\
01233310\
01222210\
00111000\
00000000\
00000000
