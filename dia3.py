from numpy import intp

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure")
op=input("You're at a cross road. Where do you want to go? 'left' or 'right'\n").lower
if(op=="left"):
    op=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower
    if(op=="wait"):
        op=input("Your arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n").lower
        if(op=="red" or op=="blue"):
            print("You enter a room of beasts. Game over.")
        elif(op=="yellow"):
            print("Your found the treasure. You win!!!")
        else:
            print("You chose a room that doesn't exist")
    else:
        print("You got attecked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")

