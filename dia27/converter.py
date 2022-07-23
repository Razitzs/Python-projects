from tkinter import *

def to_km():
    miles=float(m_input.get())
    km=miles*1.609
    result_label.config(text=f"{km}")


window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50,pady=50)

m_input=Entry(width=7)
m_input.grid(column=1,row=0)



m_label=Label(text="Miles")
m_label.grid(column=2,row=0)

equal_label=Label(text="Is equal to")
equal_label.grid(column=0,row=1)


result_label = Label(text="0")
result_label.grid(column=1,row=1)

button=Button(text="Calculate",command=to_km)
button.grid(column=1,row=2)

window.mainloop()