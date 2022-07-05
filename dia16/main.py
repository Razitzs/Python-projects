from platform import machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
import time
logo='''
                      (
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
    \""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'

'''

hola=Menu()
machine=MoneyMachine()

def isSufficient(drink):
    for i in drink.ingredients:
        if drink.ingredients[i] > hola.ingredients[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

while True:
    print(logo)
    op=input(f"What would you like? ({hola.get_items()}): ").lower()
    if op=='report':
        machine.report(hola.ingredients["water"],hola.ingredients["milk"],hola.ingredients["coffee"])
        input()
    elif op=='off':
        break
    else:
        drink=hola.find_drink(op)
        if drink.name!=None:
            if isSufficient(drink)==True:
                for i in hola.ingredients:
                    hola.ingredients[i]-=drink.ingredients[i]
                machine.make_payment(drink.cost)
                print(f"Here is your {drink.name} ☕️. Enjoy!")
                time.sleep(2)





