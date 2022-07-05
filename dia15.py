from genericpath import exists
from lib2to3.pgen2.token import NAME
from tkinter import Menu
from matplotlib.style import available
from numpy import ndim
import os

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
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
def convert(quarters,dimes, nickles,pennies):
    mquarters=quarters*0.25
    mdimes=dimes*.1
    mnickles=nickles*.05
    mpennies=pennies*.01
    total=mquarters+mdimes+mnickles+mpennies
    print(f"You entered: ${total}")
    global profit
    profit+=total
    return total

def charge(name,MENU,money):
    cost=MENU[name]['cost']
    if money>=cost:
        money-=cost
        if money>0:
            print(f"Here is ${money} in change")
        print(f"Here is your {name}. Enjoy!")
        return True
    else:
        return False


def verify(name,MENU, resources):
    waterNeeded=MENU[name]["ingredients"]["water"]
    coffeeNeeded=MENU[name]["ingredients"]["coffee"]
    waterAvailable=resources["water"]
    coffeeAvailable=resources["coffee"]
    
    if name=='espresso':
        if waterNeeded<=waterAvailable and coffeeNeeded<=coffeeAvailable:
            resources["water"]-=waterNeeded
            resources["coffee"]-=coffeeNeeded
        else:
            print("Sorry, there is not enough resources")
    else:
        milkAvailable=resources["milk"]
        milkNeeded=MENU[name]["ingredients"]["milk"]
        if waterNeeded<=waterAvailable and coffeeNeeded<=coffeeAvailable and milkNeeded<=milkAvailable:
            resources["water"]-=waterNeeded
            resources["coffee"]-=coffeeNeeded
            resources["milk"]-=milkNeeded
        else:
            print("Sorry, there is not enough resources")

buy=True
valid=True
charged=True

while buy==True:
    print(logo)
    while valid==True:
        op=input("What would you like? (espresso/latte/cappuccino): ")
        if op=='espresso' or op=='latte'or op=='cappuccino':
            valid=False  
        else:
            print("Insert a valid option")

    cost=MENU[op]['cost']
    print(f"This coffe costs: ${cost}")
    nquarters=int(input("How many quarters? "))
    ndimes=int(input("How many dimes? "))
    nnickles=int(input("How many nickels? "))
    npennies=int(input("How many pennies? "))

    total=convert(nquarters,ndimes,nnickles,npennies)
    charged=charge(op,MENU,total)
    if charged==False:
        print("Sorry that's not enough money. Money Refunded")
    else: 
        verify(op,MENU,resources)
    valid=True
    another=input("Do you want to buy something else? type 'yes' or 'no'")
    if another=='no':
        buy=False
    os.system('cls')