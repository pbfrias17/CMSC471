
import math
import random
from decimal import *

def main():
    easyVar = [5, 5, 5, 5]
    medVar = [-4, 11]
    hardVar = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
    allVar = [easyVar, medVar, hardVar]
    print("Results:")

    print("Hill Climbing")
    for i in range(3):
        var = allVar[i]
        #step = Decimal('0.1')
        step = .1
        HCmin = HillClimbing(var, i, step)
        print (HCmin)
        input()


def HillClimbing(var, difficulty, step):
    base = HCfunc(var, difficulty)
    HCmin = base + 1 
    #newVar = VAR
    resultList = list()
    index = 0
    while (index < len(var)):
        base = HCfunc(var, difficulty)
        newVar = var[:]
        newVar[index] -= step
        print(newVar)
        result = HCfunc(newVar, difficulty)
        if result > base:
            print("\tResult is greater than base!")
            newVar = var[:]
            newVar[index] += step
            #newVar[index] = math.ceil(newVar[index])
            result = HCfunc(newVar, difficulty)
            if result > base:
                print("\tSTILL BIGGER!")
                index += 1
                result = base
                newVar = var[:]
        var = newVar
                
                
    print(var)

        ##

    HCmin = base
        ###
    return HCmin
        



def HCfunc(var, num):
    if num == 0:
        return easy(var)
    elif num == 1:
        return medium(var)
    elif num == 2:
        return hard(var)


def HCstep(oldResult, result, step, index, var, i):
    newResult = oldResult
    if oldResult >= result:
        var[index] += step
        newResult = HCfunc(var, i)
    elif oldResult < result:
        step *= -1
    
        
        
    
def easy(var):
    x = var[0]
    y = var[1]
    z = var[2]
    k = var[3]
    return ((x-10)**2 + (y+8)**2 + z**2 + k**2)

def medium(var):
    x = var[0] + 100
    y = var[1] + 100
    r = x**2 + y**2
    firstPart = (math.sin(x**2+(3 * y**2))/ (.1 + r))
    secondPart = (x**2 + 5 * (y**2)) * (( math.e ** (1-r))/2)
    return -(firstPart + secondPart)



def hard(var):
    a = int(var[0])
    b = int(var[1])
    c = int(var[2])
    d = int(var[3])
    e = int(var[4])
    f = int(var[5])
    g = int(var[6])
    h = int(var[7])
    i = int(var[8])
    j = int(var[9])
    penalty = 0
    if(a < 1 or a > 3):
        penalty += abs(a-1) * 100
    if(b < 1 or b > 3):
        penalty += abs(b-1) * 100
    if(c < 1 or c > 3):
        penalty += abs(c-1) * 100
    if(d < 1 or d > 3):
        penalty += abs(d-1) * 100
    if(e < 1 or e > 3):
        penalty += abs(e-1) * 100
    if(f < 1 or f > 3):
        penalty += abs(f-1) * 100
    if(g < 1 or g > 3):
        penalty += abs(g-1) * 100
    if(h < 1 or h > 3):
        penalty += abs(h-1) * 100
    if(j < 1 or j > 3):
        penalty += abs(j-1) * 100
    if(i < 1 or i > 3):
        penalty += abs(i-1) * 100

    if(a == b):
        penalty += 1
    if(a == c):
        penalty += 1
    if(c == d):
        penalty += 1
    if(b == c):
        penalty += 1
    if(d == e):
        penalty += 1
    if(d == f):
        penalty += 1
    if(f == g):
        penalty += 1
    if(e == g):
        penalty += 1
    if(g == h):
        penalty += 1
    if(h == i):
        penalty += 1
    if(h == j):
        penalty += 1
    if(i == j):
        penalty += 1

    return penalty
    


main()
