from turtle import Turtle,Screen
from matplotlib.pyplot import table
from prettytable import PrettyTable


#timmy=Turtle()
#myScreen=Screen()
#print(myScreen.canvheight)
# timmy.shape("turtle")
# timmy.color("DeepPink")
# timmy.forward(100)
# myScreen.exitonclick()

table=PrettyTable()

table.field_names=["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", " Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)
