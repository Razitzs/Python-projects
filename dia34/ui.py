from tkinter import *
from tkinter import font

from click import command
from quiz_brain import QuizBrain
from numpy import size

THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz:QuizBrain):
        self.window=Tk()
        self.window.title("Interface")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score=Label(text="Score: 0", fg="white", bg=THEME_COLOR,font=("Courier", 20,"bold"))
        self.score.grid(row=0,column=1)
        self.canvas=Canvas(height=250, width=400, highlightthickness=0)
        self.canvas.grid(row=1, column=0,columnspan=3,pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Courier", 20)
        )
        self.quiz=quiz
        
        false= PhotoImage(file="dia34/images/false.png")
        true= PhotoImage(file="dia34/images/true.png")
        self.false_button = Button(image=false, highlightthickness=0,command=self.false_pressed)
        self.true_button = Button(image=true, highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(row=2, column=0)
        self.true_button.grid(row=2, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour final score was: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.change_color(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.change_color(is_right)

    def change_color(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)