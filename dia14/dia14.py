from random import random
from datos import data
from art import logo
from art import vs
import random
import os

score=0
lost=False
print(logo)
a=random.choice(data)

while lost==False:
    print(f'Compare A: {a["name"]}, a {a["description"]} from {a["country"]}')
    print(vs)

    b=random.choice(data)
    print(f'Compare B: {b["name"]}, a {b["description"]} from {b["country"]}')

    op=input("Who has more followers? Type 'A' or 'B': ")
    afollowers=a["follower_count"]
    bfollowers=b["follower_count"]
    if op=='A' and afollowers>bfollowers:
        score+=1
        os.system('cls')
        print(logo)
        print(f"Your're right! Current score: {score}")
        a=b
    elif op=='B' and afollowers>bfollowers:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        lost=True
    elif op=='A' and afollowers<bfollowers:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        lost=True
    elif op=='B' and afollowers<bfollowers:
        score+=1
        os.system('cls')
        print(logo)
        print(f"Your're right! Current score: {score}")
        a=b
    elif op=='A' and afollowers==bfollowers:
        score+=1
        os.system('cls')
        print(logo)
        print(f"Your're right! Current score: {score}")
        a=b
    elif op=='B' and afollowers==bfollowers:
        score+=1
        os.system('cls')
        print(logo)
        print(f"Your're right! Current score: {score}")
        a=b

