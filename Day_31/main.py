from random import choice
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
translation = ""

# ---------------------------- Generate Word List ------------------------------- #
words = {}
with open("text.txt", 'r', encoding="utf-8") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        row = data[i].split("\t")
        try:
            words[row[0]] = row[1]
        except IndexError:
            pass



# ---------------------------- Right & Wrong ------------------------------- #

def checkguess(*args):
    guess = guess_entry.get().strip()
    canvas.itemconfig(translation_text, text=translation)

    if guess.lower() == translation.lower():
        canvas.itemconfig(language_text, text="Correct! Victory Pudding!")

    else:
        canvas.itemconfig(language_text, text="Wrong! Sad Pudding... :(")


def right():
    drawnewcard()
    pass


def wrong():
    window.destroy()
    pass


def drawnewcard():
    guess_entry.delete(0, "end")
    global translation
    canvas.create_rectangle(120, 100, 720, 500, outline = "white")
    new_word = choice(list(words))
    print(new_word)
    print(words[new_word])
    translation = words[new_word]
    canvas.itemconfig(word_text, text=new_word)
    canvas.itemconfig(translation_text, text="")
    canvas.itemconfig(language_text, text="Make Your Guess!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

canvas = Canvas(width=825, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(420, 275, image=card_front)
canvas.grid(row=0, column=0, columnspan=3)

language_text = canvas.create_text(420, 125, text="Make Your Guess!", font=("Open Symbol", 20))
word_text = canvas.create_text(420, 275, text="", font=("Open Symbol", 50, "bold"), justify="center")
translation_text = canvas.create_text(420, 400, text="", font=("Open Symbol", 30, "bold"), justify="center")

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=right)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
right_button.grid(row=1, column=2)
wrong_button.grid(row=1, column=0)

guess_entry = Entry(bg="white", font=("Open Symbol", 45, "bold"), justify="center", width=10)
guess_entry.focus()
guess_entry.grid(row=1, column=1, sticky="NESW")


drawnewcard()


window.bind('<Return>', checkguess)
window.mainloop()
