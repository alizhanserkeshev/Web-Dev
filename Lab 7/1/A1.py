import math 

def funct(a, b):
    return math.sqrt(a**2 + b**2)

leg1 = float(input())
leg2 = float(input())

hypotenuse = funct(leg1, leg2)
print(hypotenuse)
