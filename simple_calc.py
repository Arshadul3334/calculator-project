import math
import time

def add(x,y):
    print(x+y)

def subtraction(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)

def division(x,y):
    if y==0 :
        print('Division by 0 is not possible')
    else:
        print(round(x/y))

def percent(x,y):
    print(x*(y/100))

def exponent(x,y):
    print(pow(x,y))

def squareroot(x):
    print(math.sqrt(x))

def remainders(x,y):
    print(x % y)

def onlynumbers(e):
    while True:
        try:
            return float(input(e))
        except ValueError:
            print("Please enter valid numbers!")
            time.sleep(2)
            continue
def choice():
    while True:
        try:
            Choice = int(input('Please select which operation you would like to do :\n 1. Multiply \n 2.Divide \n 3.Add \n 4.Substract \n 5.Percentage\n 6.Power\n 7.Square root \n 8.Remainder \n 9.Exit \n'))
            return Choice
        except ValueError:
            print("Please enter a valid option")
            time.sleep(2)
            continue
while True:
    Choice = choice()
    
    if Choice == 1:
        x = onlynumbers('Type the 1st number : \n')
        y = onlynumbers('Type the 2nd number : \n')
        multiply(x,y)

    elif Choice == 2:
        x = onlynumbers('Type the 1st number : \n')
        y = onlynumbers('Type the 2nd number : \n')
        division(x,y)

    elif Choice == 3:
        x = onlynumbers('Type the 1st number : \n')
        y = onlynumbers('Type the 2nd number : \n')
        add(x,y)

    elif Choice == 4:
        x = onlynumbers('Type the 1st number : \n')
        y = onlynumbers('Type the 2nd number : \n')
        subtraction(x,y)

    elif Choice == 5:
        x = onlynumbers('Type the Whole number : \n')
        y = onlynumbers('Type the Percentage of that you want : \n')
        percent(x,y)

    elif Choice == 6:
        x = onlynumbers('Type the Number you want exponent of : \n')
        y = onlynumbers('Type the exponent : \n')
        exponent(x,y)

    elif Choice == 7:
        x = onlynumbers('Type the Number you want square root of : \n')
        squareroot(x)

    elif Choice == 8:
        x = onlynumbers('Type the 1st number : \n')
        y = onlynumbers('Type the 2nd number : \n')
        remainders(x,y)

    elif Choice == 9:
        print('Bye!')
        break
    else:
        print('Please enter a valid option')
