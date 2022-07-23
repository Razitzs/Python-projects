from ast import Pass, Raise
import json

from tkinter import *
from tkinter import messagebox
import numbers
import random
import string


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#2b3e33"
BLUE="#648cbb"
BLACK="#000000"
WHITE = "#ffffff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters=4
    symbols=2
    numbers=2

    lett=""
    for i in range(0,letters):
        lett+=random.choice(string.ascii_letters)

    sym=""
    simbolos="!@#$%^&*()_"
    for i in range(0,symbols):
        sym+=random.choice(simbolos)

    num=""
    for i in range(0,numbers):
        num+=str(random.randint(0,10))

    password=lett+sym+num

    passw =""
    for i in range(0,len(password)):
        passw += random.choice(password[random.randint(0,(len(password)-1))])
    password_entry.insert(0,passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    web=w_entry.get()
    user=EmUsr_entry.get()
    pswd=password_entry.get()
    n_data={
        web: 
        {
            "email":user,
            "password":pswd,
        }
    }
    if len(web)==0 or len(user)==0 or len(pswd)==0:
        messagebox.showinfo("Please don't leave any fields empty.")
    else:
        ok=messagebox.askokcancel(title=web, message=f"The data you entered is: {web}, {user}, {pswd}. \nPress ok to continue...")
        if ok:
            try:
                with open("dia29y30/data.json", "r") as f:
                    data = json.load(f)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("dia29y30/data.json", "w") as f:
                    json.dump(n_data, f, indent=4)
            else:
                data.update(n_data)
                with open("dia29y30/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                w_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH INFO ------------------------------- #
def search_info():
    web=w_entry.get()
    with open("dia29y30/data.json", "r") as f:
        try:
            data = json.load(f)
            messagebox.showinfo(title="Info",message=f"Email: {data[web]['email']}\nPassword: {data[web]['password']}")
        except FileNotFoundError:
            messagebox.showinfo(title="Info",message=f"Data file not found")
        except KeyError:
            messagebox.showinfo(title="Info",message=f"No details for {web} exists")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password generator")
window.config(padx=20,pady=20, bg=WHITE)
canvas=Canvas(height=200, width=200, bg=WHITE, highlightthickness=0)
canvas.grid(column=1,row=1)
image=PhotoImage(file="dia29y30/logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(column=1,row=0)

website=Label(text="Website: ", fg=BLACK, bg=WHITE,font=("Arial", 14))
website.grid(column=0,row=1)
w_entry=Entry(width=35)
w_entry.grid(column=1,row=1)
w_entry.focus()
EmUsr=Label(text="Email/Username: ", fg=BLACK,bg=WHITE,font=("Arial", 14))
EmUsr.grid(column=0,row=2)
EmUsr_entry=Entry(width=35)
EmUsr_entry.grid(column=1,row=2)
EmUsr_entry.insert(0, "razovilledafernando@gmail.com")
password=Label(text="Password: ", fg=BLACK,bg=WHITE,font=("Arial", 14))
password.grid(column=0,row=3)
password_entry=Entry(width=35)
password_entry.grid(column=1,row=3)
add=Button(text="Add",font=("Arial", 8), width=36, command=save_info)
add.grid(column=1,row=4)
generate=Button(text="Generate",font=("Arial", 8), width=23, command=generate_password)
generate.grid(column=3,row=3)
search=Button(text="Search",font=("Arial", 8), width=23, command=search_info)
search.grid(column=3,row=1)

window.mainloop()