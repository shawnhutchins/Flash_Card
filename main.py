from tkinter import *

# ---------------------------------- Tasks -------------------------------- #

#Constants
BACKGROUND_COLOR = "#B1DDC6"

images = ["images/card_front.png",
          "images/card_back.png",
          "images/right.png",
          "images/wrong.png"]

window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ------------------------------ User Interface --------------------------- #

# ---------------------------------- Layout ------------------------------- #

window.mainloop()