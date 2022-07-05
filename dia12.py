import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

def compare(lives,guess,choice):
    if(guess>choice):
        print("Too high")
        lives-=1
        print(f"You have {lives} attempts remaining to guess the number")
        return lives,False
    elif(guess<choice):
        print("Too low")
        lives-=1
        print(f"You have {lives} attempts remaining to guess the number")
        return lives,False
    elif(guess==choice):
        return lives,True
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

choice=random.randint(1,100)
#print(f"The answer is: {choice}")
win=False
op=input("Choose a difficulty. Type 'easy' or 'hard': ")
if op=='easy':
    lives=10
    print(f"You have {lives} attempts remaining to guess the number")
    while(lives>0 and win==False):
        guess=int(input("Make a guess: "))
        lives,win=compare(lives,guess,choice)
elif op=='hard':
    lives=5
    print(f"You have {lives} attempts remaining to guess the number")
    while(lives>0 and win==False):
        guess=int(input("Make a guess: "))
        lives,win=compare(lives,guess,choice)

if(win==True):
    print(f"You got it! The answer was {choice}.")
elif(win==False):
    print("You've run out of guesses, you lose")

