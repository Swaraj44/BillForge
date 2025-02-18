from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from PIL import Image, ImageTk, ImageSequence

import GeneralGuiLogin as GLIG
import BacklogGuiLogin as GBLL
import os
import sys

#For Relative Resource Path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





# Get the current script's directory
SCRIPT_PATH = Path(__file__).parent

ASSETS_PATH = SCRIPT_PATH

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize the Tkinter window
window = Tk()
window.geometry("751x451")
window.configure(bg="#F0F0F0")
window.title("BillForge - KUET Teachers’ Edition")  # Set the window title
#icon_path = r"assets_welcomescrseen\frame0\logo.ico"  # Full path to your .ico file
window.iconbitmap(relative_to_assets(resource_path('data\\images\\general_logo.ico')))

# Create a canvas
canvas = Canvas(
    window,
    bg="#F0F0F0",
    height=451,
    width=751,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# # Load Static Image using full directory path
# image_path = r"assets_welcomescreen\frame0\image_1.png"  # Full path to the image
# image_image_1 = PhotoImage(file=resource_path('data\\images\\'))
# image_1 = canvas.create_image(375.0, 219.0, image=image_image_1)

# Load Animated GIF using full directory path
#gif_path = r"assets_welcomescreen\frame0\Wlc_Screen_3.gif"  # Full path to the GIF
gif_image = Image.open(resource_path('data\\images\\Wlc_Screen_3_gui.gif'))
frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif_image)]
gif_label = Label(window)
gif_label.place(x=50, y=75)  # Adjust to your preferred position

def animate_gif(frame=0):
    frame_image = frames[frame]
    gif_label.config(image=frame_image)
    gif_label.image = frame_image  # Keep a reference
    window.after(50, animate_gif, (frame + 1) % len(frames))  # Adjust delay as needed

# Start GIF animation
animate_gif()

# Define fun1 function to handle button_1 click
def fun1():
    #print("button_1 clicked")
    window.destroy()
    GLIG.LOGIN_GENERAL()
    
    
    
def fun2():
    #print("button_1 clicked")
    window.destroy()
    GBLL.LOGIN_BACKLOG()
    

# Load Button Images using full directory path
#button_image_1_path = r"assets_welcomescreen\frame0\button_1.png"  # Full path to button image
button_image_1 = PhotoImage(file=resource_path('data\\images\\button_1.png'))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=fun1,  # Call fun1 when button_1 is clicked
    relief="flat"
)
button_1.place(x=301.0, y=370.0, width=150.0, height=30.0)

#button_image_2_path = r"assets_welcomescreen\frame0\button_2.png"  # Full path to button image
button_image_2 = PhotoImage(file=resource_path('data\\images\\button_2.png'))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=fun2,  # Call fun1 when button_2 is clicked
    relief="flat"
)
button_2.place(x=301.0, y=407.0, width=150.0, height=30.0)

# Canvas text
canvas.create_text(
    200.0,
    15.0,
    anchor="nw",
    text="BillForge KUET Teachers’ Edition",
    fill="#000000",
    font=("Imprima Regular", 26 * -1)
)

canvas.create_text(
    300.0,
    49.0,
    anchor="nw",
    text="A Modern Billing Solution",
    fill="#000000",
    font=("Imprima Regular", 16 * -1)
)

# Run the Tkinter main loop
window.resizable(False, False)
window.mainloop()
