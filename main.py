from tkinter import *
import csv

# ---------------------------------- Tasks -------------------------------- #
#Try opening the images to prevent an error

#Constants
BACKGROUND_COLOR = "#B1DDC6"

data = []
images = ["images/card_front.png",
          "images/card_back.png",
          "images/wrong.png",
          "images/right.png"]

with open("data/french_words.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)
    for row in reader:
        data.append(row)

# ------------------------------ User Interface --------------------------- #

window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard_canvas = Canvas(master=window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_initial_image = PhotoImage(file=images[0])
flashcard_canvas.create_image(400, 263, image=flashcard_initial_image)

language_text = flashcard_canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = flashcard_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_button_image = PhotoImage(file=images[2])
wrong_button = Button(master=window, image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR)

right_button_image = PhotoImage(file=images[3])
right_button = Button(master=window, image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR)

# ---------------------------------- Layout ------------------------------- #

flashcard_canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()