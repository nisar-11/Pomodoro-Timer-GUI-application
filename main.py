from tkinter import *
import math
from tkinter import messagebox
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
timers = None

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=90, bg=YELLOW)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_used():
    global timers
    window.after_cancel(timers)
    timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(text, text="00:00")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_used():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        timer.config(text="BREAK", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        messagebox.showinfo(title="BREAK", message="Now it's for you to take a 20 minutes long break as you completed 4 sets of WORK session.")
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="BREAK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        messagebox.showinfo(title="BREAK", message="Now its time for you to take a short break of 5 minutes as you completed your WORK session")
        countdown(break_sec)
    else:
        timer.config(text="WORK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        messagebox.showinfo(title="WORK", message="Now its time for you to get back to WORK !")
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(value):
    count_min = math.floor(value / 60)
    if count_min < 10:
        count_min = "0"+f"{count_min}"
    count_sec = value % 60
    if count_sec < 10:
        count_sec = "0"+f"{count_sec}"
    if value >= 0:
        global timers
        canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
        timers = window.after(1000, countdown, value - 1)
    else:
        start_used()
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += "✓"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# canvas creation


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=1)


start = Button(text="Start", command=start_used, highlightthickness=0)
start.grid(column=0, row=3)


reset = Button(text="Reset", command=reset_used, highlightthickness=0)
reset.grid(column=2, row=3)


check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check.grid(column=1, row=4)

window.mainloop()
