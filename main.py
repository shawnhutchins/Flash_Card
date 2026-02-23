from tkinter import *

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

flashcard_canvas = Canvas(master=window, width=800, height=526, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
flashcard_initial_image = PhotoImage(file=images[0])
flashcard_canvas.create_image(400, 263, image=flashcard_initial_image)

# ---------------------------------- Layout ------------------------------- #

flashcard_canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()