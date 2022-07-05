import numbers
import random
import string

print("Welcome to the password generator!!!\n")
letters=int(input("How many letters would you like in your password?\n"))
symbols=int(input("How many symbols would you like?\n"))
numbers=int(input("How many numbers would you like?\n"))

lett=""
for i in range(0,letters):
    lett+=random.choice(string.ascii_letters)
#print(f"\nlett: {lett}")

sym=""
simbolos="!@#$%^&*()_"
for i in range(0,symbols):
    sym+=random.choice(simbolos)
#print(f"Sym: {sym}")

num=""
for i in range(0,numbers):
    num+=str(random.randint(0,10))
#print(f"Num: {num}")

password=lett+sym+num
#print(f"Password: {password}\n")

passw =""
for i in range(0,len(password)):
    passw += random.choice(password[random.randint(0,(len(password)-1))])
print(f"\nHere is your password: {passw}\n")

