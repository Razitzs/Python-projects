import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculate(num1: float,operator:str,num2:float)->float:
    if operator=="+":
        print(num1)
        return num1+num2
    elif operator=="-":
        print(num1)
        return num1-num2
    elif operator=="*":
        print(num1)
        return num1*num2
    elif operator=="/":
        print(num1)
        return num1/num2

def nextNumber(num):
    print("+\n-\n*\n/")
    operator=input("Pick an operator: ")
    num2=float(input("What's the next number? "))
    r=calculate(num,operator,num2)
    print(f"{num}{operator}{num2}={r}")
    op=input(f"Type 'y' to continue calculating with {r}, or type 'n' to start a new calculation: ")
    if op=='y':
        return r,True
    return r,False

b=True
while b==True:
    os.system('cls')
    print(logo)
    num=float(input("What's the first number? "))
    result=0
    result,op=nextNumber(num)
    while op==True:
        result,op=nextNumber(result)









