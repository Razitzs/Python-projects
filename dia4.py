import random
import string

def printPlayers(user: str, cpu: str):
    print("You chose: \n")
    print(user)
    print("\nComputer chose: \n")
    print(cpu)

def winner(user: int, cpu: int):
    if user==0:
        if cpu==0:
            print("Tie")
        elif cpu==1:
            print("You lose")
        elif cpu==2: 
            print("You win!!!")
    if user==1:
        if cpu==0:
            print("You win!!!")
        elif cpu==1:
            print("Tie")
        elif cpu==2: 
            print("You lose")
    if user==2:
        if cpu==0:
            print("You lose")
        elif cpu==1:
            print("You win!!!")
        elif cpu==2: 
            print("Tie")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
cpu=random.randint(0,2)
if(cpu==0):
    scpu=rock 
elif cpu==1:
    scpu=paper
elif cpu==2:
    scpu=scissors

op=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors."))
if(op==0):
    user=rock
    printPlayers(user,scpu)
    winner(op,cpu)
elif op==1:
    user=paper
    printPlayers(user,scpu)
    winner(op,cpu)
elif op==2:
    user=scissors
    printPlayers(user,scpu)
    winner(op,cpu)
else:
    print("You typed an invalid number, you lose!")

