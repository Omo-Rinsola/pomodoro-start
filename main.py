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
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global my_timer
    window.after_cancel(my_timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

    elif reps == 8:
        timer_label.config(text="Work", fg=RED)
        countdown(long_break_secs)

    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_secs)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = "✓"
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✓'
        check.config(text=marks)


# window.after(1000) the time is in milli seconds
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# to put the image at the center of the canvas, divide the width and height by 2
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)


# Labels
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 38))
timer_label.grid(column=1, row=0)
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check.grid(column=1, row=3)

# BUTTON
start = Button(text="start", bg=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)
window.mainloop()
