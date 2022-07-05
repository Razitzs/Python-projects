from ast import match_case
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, Decimal
from pydoc import doc
from decimal import Decimal
import string
from unicodedata import decimal


print("Welcome to the tip calculator ")
total=input("What was the total bill? ")
t=float(total)
people=input("How many people to split the bill? ")
p=int(people)
b=True
while b==True:
    percentage=input("What percentage would you like to give? 10, 12 or 15? ")
    if(percentage=="10"):
        t*=1.10
        b=False
    elif(percentage=="12"):
        t*=1.12
        b=False
    elif(percentage=="15"):
        t*=1.15
        b=False
    else:
        print("Write a valid percentage")

each=t/p
print(f"Each person should pay: ${round(each,2)}")

