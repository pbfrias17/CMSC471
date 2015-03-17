import math
import random
from decimal import *

def main():
    easyVar = [5, 5, 5, 5]
    medVar = [-4, 11]
    hardVar = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]
    allVar = [easyVar, medVar, hardVar]
    print("Results:")


    for i in range(1):
        GSmin = GeneticSearch(allVar[i], i)
        print(GSmin)


def GeneticSearch(var, num):
    count = 1000
    hold = newVar[:]
    randIncr = random.randint(1, 2)
    randIndex = random.randint(0, len(var)-1)
    if randIncr == 1:
        newVar[randIndex] -= varStep
    else:
        newVar[randIndex] += varStep

    newVal = GenFunc(newVar, num)



main()
