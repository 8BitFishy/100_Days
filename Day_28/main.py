from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        duration = LONG_BREAK_MIN
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        duration = SHORT_BREAK_MIN
    else:
        timer_label.config(text="Work", fg=GREEN)
        duration = WORK_MIN

    countdown(duration * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps
    global timer
    seconds = count % 60
    minutes = math.floor(count / 60)

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text = marks)
        start()

    # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas_width = 224
canvas_height = 248
canvas = Canvas(width=canvas_width, height=canvas_height, bg=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(canvas_width/2, canvas_height/2, image=bg)
timer_text = canvas.create_text(canvas_width/2, canvas_height/2 + 20, text="00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start",  font=(FONT_NAME, 12, "normal"), highlightthickness=0, relief = "groove", command=start)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, relief = "groove", command=reset)
reset_button.grid(row=3, column=2)

check_label = Label(bg = YELLOW, fg = GREEN, font = (FONT_NAME, 12, "normal"))
check_label.grid(row=4, column=1)
























window.mainloop()