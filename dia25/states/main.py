from email.errors import MissingHeaderBodySeparatorDefect
import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
t=turtle.Turtle()
t.hideturtle()
t.penup()

image="dia25/states/blank_states_img.gif"
screen.addshape(image) #Esto es para que la pantalla tenga la resolución de la imagen de los estados
turtle.shape(image) # Esto es para la pantalla contenga la imagen de los estados
num_states=1

data=pandas.read_csv("dia25/states/50_states.csv")
states=data.state.tolist()
correct_states=[]

while num_states<50:
    answer_state=screen.textinput("States", "Please enter the state you want").title()
    screen.title(f"{num_states}/50 States Correct")
    if answer_state=="Exit":
        break

    if answer_state in states:
        s=data[data["state"]==answer_state]
        t.goto(int(s.x),int(s.y))
        t.write(f"{answer_state}")
        correct_states.append(answer_state)
        num_states+=1

missing_states=set(states).difference(correct_states)
f=pandas.DataFrame(missing_states)
f.to_csv("dia25/states/missing_states.csv")
turtle.mainloop()
