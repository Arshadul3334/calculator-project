import math
import time

def add(x,y):
    return (x+y)

def subtraction(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def division(x,y):
    if y==0 :
        return ('Division by 0 is not possible')
    else:
        return (round(x/y))

def percent(x,y):
    return (x*(y/100))

def exponent(x,y):
    return (pow(x,y))

def squareroot(x):
    return (math.sqrt(x))

def remainders(x,y):
    return (x % y)

def onlynumbers(e):
    while True:
        try:
            float(e)
            return True
        except ValueError:
            return False



if __name__ == "__main__":
    pass