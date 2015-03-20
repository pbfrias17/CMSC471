import math
import random
from decimal import *

def main():
    easyVar = [5, 5, 5, 5]
    medVar = [-4, 11]
    hardVar = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    allVar = [easyVar, medVar, hardVar]
    print("Results:")


    for i in range(3):
        GSmin = GeneticSearch(allVar[i], i)
        print(GSmin)


def GeneticSearch(var, num):
    #basically, start with two identical parents that have
    # 5 children each, then the best child from each parent
    # mate twice and that process is repeated.
    totalGen = 100
    offspringList = [var, var]
    while totalGen > 0:
        totalGen -= 1
        for i in range(2):
            result = -100
            for j in range(5):
                newVar = offspringList[i][:]
                randIncr = random.randint(-5, 5)
                randIndex = random.randint(0, len(var)-1)
                newVar[randIndex] += randIncr / 2
                newResult = GenFunc(newVar, num)
                if result < 0 or newResult < result:
                    result = newResult
                    offspringList[i] = newVar
        bestOffspring = crossover(offspringList)
        offspringList = [bestOffspring, bestOffspring]

    return GenFunc(bestOffspring, num)


def crossover(matrix):
    offspring = []
    for y in range(len(matrix[0])):
        offspring.append((matrix[0][y] + matrix[1][y]) / 2)
        
    return offspring
        



def GenFunc(var, num):
    if num == 0:
        return easy(var)
    elif num == 1:
        return medium(var)
    elif num == 2:
        return hard(var)



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

