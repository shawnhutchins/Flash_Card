from tkinter import *
import random
import pandas

# ---------------------------------- Tasks -------------------------------- #
#Try opening the images to prevent an error

#Constants
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_ONE = "French"
LANGUAGE_TWO = "English"
FLIP_DELAY_MS = 3000

images = ["images/card_front.png",
          "images/card_back.png",
          "images/wrong.png",
          "images/right.png"]

dataframe = pandas.read_csv("data/french_words.csv")
data = dataframe.to_dict(orient="records")
current_flashcard = {}

def flip_flashcard():
    global current_flashcard
    flashcard_canvas.itemconfig(flashcard_canvas_image, image=flashcard_back_image)
    flashcard_canvas.itemconfig(language_text, text=LANGUAGE_TWO)
    flashcard_canvas.itemconfig(word_text, text=current_flashcard[LANGUAGE_TWO])

#Updates the text values on the canvas with a random word
def next_flashcard():
    global current_flashcard
    flashcard_canvas.itemconfig(flashcard_canvas_image, image=flashcard_front_image)
    current_flashcard = random.choice(data)
    flashcard_canvas.itemconfig(language_text, text=LANGUAGE_ONE)
    flashcard_canvas.itemconfig(word_text, text=current_flashcard[LANGUAGE_ONE])

    window.after(FLIP_DELAY_MS, flip_flashcard)

# ------------------------------ User Interface --------------------------- #
window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard_front_image = PhotoImage(file=images[0])
flashcard_back_image = PhotoImage(file=images[1])

#Canvas
flashcard_canvas = Canvas(master=window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_canvas_image = flashcard_canvas.create_image(400, 263, image=flashcard_front_image)

language_text = flashcard_canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = flashcard_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

#Buttons
wrong_button_image = PhotoImage(file=images[2])
wrong_button = Button(master=window, image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_flashcard)

right_button_image = PhotoImage(file=images[3])
right_button = Button(master=window, image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_flashcard)

# ---------------------------------- Layout ------------------------------- #
#Canvas
flashcard_canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

#Initializing flashcard_canvas text
next_flashcard()

window.mainloop()