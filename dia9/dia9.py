import os
from unicodedata import name
from art import logo
bids={}
print(logo)
while True:
  name=input("Write the name of the bidder: ")
  bid=float(input("Enter the bid: "))
  bids[name]=bid
  op=int(input("Is there another user that wants to bid? 1) yes  2) no"))
  if op==2:
    os.system('cls')
    break
  os.system('cls')

print(bids)

count=0
for key in bids:
  if count==0:
    highest=bids[key]
    highestName=key
  if highest<bids[key]:
    highest=bids[key]
    highestName=key
  count+=1

print(f"The winner is {highestName} with a bid of ${highest}")




