from tkinter import *
import math
import webbrowser

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2b3e33"
BLUE="#648cbb"
BLACK="#000000"
WHITE = "#ffffff"
WORK_MIN = 25
SHORT_BREAK_MIN =5 
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="The Last Of Breaks", fg=BLUE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="The Last Of Work", fg=RED)
        webbrowser.open('https://www.youtube.com/watch?v=Dy1EW9VBoCQ') 
        
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text, text="00:00")
    title.config(text="The Last Of Timers",fg=BLACK)
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("The Last Of Pomodoro Timers")
window.config(padx=100,pady=100, bg=GREEN)

canvas=Canvas(bg=GREEN, highlightthickness=0)
canvas.grid(column=1,row=1)
image=PhotoImage(file="dia28/tlou.png")
canvas.create_image(190,120, image=image)
text=canvas.create_text(190,240, text="00:00",font=("Headliner",25,"bold"),fill="white")
canvas.grid(column=100,row=1)
title=Label(text="The Last Of Timers", fg=BLACK,bg=GREEN,font=("Headliner", 35, "bold"))
title.grid(column=100,row=0)

start=Button(text="Start",font=("Headliner", 20), command=start_timer)
start.grid(column=0,row=2)
reset=Button(text="Reset",font=("Headliner", 20),command=reset_timer)
reset.grid(column=1000,row=2)
checkmark=Label(fg=WHITE,bg=GREEN, font=("Headliner", 20)) 
checkmark.grid(column=100,row=3)
window.mainloop()
