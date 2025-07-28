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
        print(x/y)

def percent(x,y):
    print(x*(y/100))

def onlynumbers(e):
    while True:
        try:
            return float(input(e))
        except ValueError:
            print("Please enter valid numbers!")
            continue

    
while True:
    Choice = int(input('Please select which operation you would like to do : 1. Multiply , 2.Divide , 3.Add , 4.Substract , 5.Percentage, 6.Exit \n'))
    
    
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
        print('Bye!')
        break
    else:
        print('Please enter a valid option')