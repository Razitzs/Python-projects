import tkinter
from tkinter import font
from turtle import width
from matplotlib.pyplot import text

from pyparsing import common_html_entity
from setuptools import Command

def button_pressed():
    text=i.get()
    label["text"]=text



window=tkinter.Tk()
window.title("GUI")
window.minsize(500,300)

label=tkinter.Label(text="Label", font=("Courier",24,"bold"))
label.pack()


i=tkinter.Entry(width=10)
button=tkinter.Button(text="Click Me", font=("Courier",10), command=button_pressed)
button.pack()

i.pack()









window.mainloop()



#Así se hace una función con un número indefinido de parámetros (se pasan como tupla, también se pueden acceder a los índices de la tupla)
# def add(*nums):
#     total=0
#     for n in nums:
#         total+=n
#     print(total)

# #Ahora puedo pasar valores por nombre (se pasa como diccionario) se tiene que especificar el nombre de la variable
# def calculate(**kwargs): 
#     print(kwargs)

# add(3,5,6,2,1,7,4,3)
# calculate(hola=5,adios=10)


