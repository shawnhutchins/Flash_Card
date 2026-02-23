from tkinter import *
from PIL import Image, ImageTk
# ---------------------------------- Tasks -------------------------------- #

#Constants
BACKGROUND_COLOR = "#B1DDC6"

images = ["images/card_front.png",
          "images/card_back.png",
          "images/right.png",
          "images/wrong.png"]

# ------------------------------ User Interface --------------------------- #

window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard_canvas = Canvas(master=window)

# ---------------------------------- Layout ------------------------------- #

flashcard_canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()