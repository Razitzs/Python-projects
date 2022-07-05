import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""           

def compare(score,cscore,ycards,ccards):
    print("\n---------------------------------------------------------")
    if score==21 and len(ycards)==2:
        print("You win with a blackjack!!! ಠoಠ")
    elif cscore==21 and len(ccards)==2:
        print("The oponent wins with a blackjack ┌∩┐(ಠ_ಠ)┌∩┐")
    elif score>21 and cscore>21:
        print("Both went over, both lose ( ͡ಠ ʖ̯ ͡ಠ)")
    elif score>cscore and score<=21:
        print("You win!!! ( ͡° ͜ʖ ͡°)")
    elif score<cscore and cscore<=21:
        print("The computer wins ಠ益ಠ")
    elif score==cscore and score<21 and score<21:
        print("Draw ¯\_(ツ)_/¯")
    elif cscore>21 and score <21:
        print("Opponent went over ( ͡° ͜ʖ ͡°) You win!!!")
    elif cscore<21 and score>21:
        print("You went over. You lose ಥ_ಥ")
    
    print(f"\nYour final score: {score}     your cards: {ycards}")
    print(f"Cpu's final score: {cscore}    CPU's cards: {ccards}")
    print("---------------------------------------------------------")

def moreCards(cards,cartas,score):
    cartas.append(random.choice(cards))
    carta=cartas[-1]
    score+=carta
    return cartas,score

def game()->bool:
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    print(logo)
    score=0
    CScore=0
    yourCards=[]
    CCards=[]
    for i in range(2):
        yourCards.append(random.choice(cards))
        score+=yourCards[i]
        CCards.append(random.choice(cards))
        CScore+=CCards[i]

    while CScore<17:
        CCards,CScore=moreCards(cards,CCards,CScore)

    print(f"\nYour cards: {yourCards}, current score: {score}")
    print(f"Computer's first card: {CCards[0]}")
    another=True
    while another==True:
        more=input("Type 'y' to get another card, type 'n' to pass:")
        if more=='y':
            yourCards,score=moreCards(cards,yourCards,score)
            print(f"Your cards: {yourCards}, current score: {score}")
            print(f"Computer's first card: {CCards[0]}")
            if(score>21 or CScore>21):
                compare(score,CScore,yourCards,CCards)
                another=False
        elif more=='n':
            another=False
            compare(score,CScore,yourCards,CCards)
    op=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if(op=='y'):
        return True
    else:
        return False

play=True
while play==True:
    os.system('cls')
    play=game()
