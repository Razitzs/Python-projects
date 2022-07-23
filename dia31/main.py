from tkinter import *
from pandas import *
import random

BLACK="#000000"
WHITE = "#ffffff"
BACKGROUND_COLOR = "#B1DDC6"
word=""

try:
    words=read_csv("dia31/data/unknown_words.csv")
except FileNotFoundError:
    words = read_csv("dia31/data/germanwords.csv")
    words_dict= {row.German:row.Spanish for (index, row) in words.iterrows()}
else:
    words_dict = {row.German:row.Spanish for (index, row) in words.iterrows()}

def show_answer(words_dict,word):
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(card_title, text="Spanish", fill=WHITE)
    canvas.itemconfig(german_word, text=words_dict[word], fill=WHITE)

def random_word():
    global timer, words_dict, word
    canvas.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=front)
    word=random.choice(list(words_dict))
    canvas.itemconfig(card_title, text="German", fill=BLACK)
    canvas.itemconfig(german_word, text=word, fill=BLACK)
    timer=canvas.after(3000, show_answer,words_dict,word)

def known():
    global words_dict,word
    words_dict.pop(word,words_dict[word])
    unknown_words =DataFrame(list(words_dict.items()),columns = ['German','Spanish']) 
    unknown_words.to_csv("dia31/data/unknown_words.csv", index=False)
    random_word()

window=Tk()
window.title("Password generator")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
canvas=Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0, columnspan=3, rowspan=4)
timer=canvas.after(0, random_word)
right=PhotoImage(file="dia31/images/right.png")
wrong=PhotoImage(file="dia31/images/wrong.png")
front=PhotoImage(file="dia31/images/card_front.png")
back=PhotoImage(file="dia31/images/card_back.png")
canvas_image=canvas.create_image(400,263,image=front)
card_title=canvas.create_text(400,150,text="German",font=("Courier", 40, "italic"))
german_word=canvas.create_text(400,300,text="",font=("Courier", 60,"bold"))
right_button=Button(image=right, highlightthickness=0, command=known)
wrong_button=Button(image=wrong, highlightthickness=0,command=random_word)
wrong_button.grid(column=0,row=4)
right_button.grid(column=2,row=4)

window.mainloop()