from tkinter import *
import random
import pandas

# ---------------------------------- Tasks -------------------------------- #
#Try opening the images to prevent an error

#Constants
BACKGROUND_COLOR = "#B1DDC6"

images = ["images/card_front.png",
          "images/card_back.png",
          "images/wrong.png",
          "images/right.png"]

dataframe = pandas.read_csv("data/french_words.csv")
data = dataframe.to_dict(orient="records")
current_word ={}

#Sets the current_word global to a new random word from the data list
def new_random_word():
    global current_word
    current_word = random.choice(data)

#Updates the text values on the canvas with a new random word
def update_flashcard_front():
    new_random_word()
    flashcard_canvas.itemconfig(language_text, text="French")
    flashcard_canvas.itemconfig(word_text, text=current_word["French"])

# ------------------------------ User Interface --------------------------- #
window = Tk()
window.title("Flash Card")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
flashcard_canvas = Canvas(master=window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_initial_image = PhotoImage(file=images[0])
flashcard_canvas.create_image(400, 263, image=flashcard_initial_image)

language_text = flashcard_canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = flashcard_canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

#Initializing flashcard_canvas text
update_flashcard_front()

#Buttons
wrong_button_image = PhotoImage(file=images[2])
wrong_button = Button(master=window, image=wrong_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=update_flashcard_front)

right_button_image = PhotoImage(file=images[3])
right_button = Button(master=window, image=right_button_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=update_flashcard_front)

# ---------------------------------- Layout ------------------------------- #
#Canvas
flashcard_canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()