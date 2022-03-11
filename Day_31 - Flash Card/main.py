import time
from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
not_known = {}
# ---------------------------- Generate Word List ------------------------------- #
'''
words = {}
english = []
hindi = []
with open("text.txt", 'r', encoding="utf-8") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        row = data[i].split("\t")
        try:
            english.append(row[1])
            hindi.append(row[0])
        except IndexError:
            pass

words["Hindi"] = hindi
words["English"] = english

print("Generating dataframe")
words_dataframe = pandas.DataFrame.from_dict(words)
words_dataframe.to_csv("hindi.csv", index=False)


'''

try:
    data = pandas.read_csv("words_to_learn.csv")
    print("Drawing from words to learn")

except FileNotFoundError:
    data = pandas.read_csv("hindi.csv")
    print("Drawing from hindi")
to_learn = data.to_dict(orient="records")

print(to_learn)





# ---------------------------- Right & Wrong ------------------------------- #

def check_card():
    #canvas.itemconfig(rectangle, state='hidden')
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")


def right():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index = False)
    drawnewcard()

def wrong():
    drawnewcard()


def drawnewcard():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    #canvas.itemconfig(rectangle, state='normal')
    current_card = choice(to_learn)
    print(current_card)
    canvas.itemconfig(word_text, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(language_text, text="Hindi", fill="black")
    flip_timer = window.after(3000, check_card)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
flip_timer = window.after(3000, check_card)


canvas = Canvas(width=825, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(420, 275, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
#rectangle = canvas.create_rectangle(120, 100, 720, 500, outline="white")

language_text = canvas.create_text(420, 125, text="Title", font=("Ariel", 40, 'italic'), justify="center")
word_text = canvas.create_text(420, 275, text="Word", font=("Ariel", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=right)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)


drawnewcard()
window.mainloop()
