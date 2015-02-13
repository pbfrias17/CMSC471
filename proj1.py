#CS471
#Proj 1 - BFS, DFS, UCS
#Paolo Frias
#Due: 02/17/1992

import sys


def main():
    CONST_OFFSET = 64
    ######
    sys.argv = [sys.argv[0], 'inputTextFile.txt', 'Breadth', 'A', 'K', 'outputFile.txt']
    ######

    startNode = ord(sys.argv[3]) - CONST_OFFSET - 1
    endNode = ord(sys.argv[4]) - CONST_OFFSET - 1
    masterList = list()
    
    #Input redirection
    file = open(sys.argv[1], "r")
    for line in file:
        for word in line.split(" "):
            masterList.append(word.rstrip())

    matrix = createMatrix(masterList)

    if sys.argv[2] == 'Breadth':
        doBFS(startNode, endNode, matrix)

    
            
def createMatrix(_list):
    CONST_OFFSET = 64
    largest = 0

    
    #create empty graph matrix of appropriate girth
    for idx, val in enumerate(_list):
        if len(_list[idx]) <= 1:
            if ord(_list[idx]) > 64 and ord(_list[idx]) < 90:
                _list[idx] = ord(_list[idx]) - CONST_OFFSET - 1
                if largest < _list[idx]:
                    largest = _list[idx]

    matrix = [[0 for x in range(largest + 1)] for y in range(largest + 1)]

    #fill matrix by iterating through list in groups of three
    itr = 0
    for x_i in range(0,len(_list),3):
        y_i = x_i + 1
        weight_i = y_i + 1
        matrix[_list[x_i]][_list[y_i]] = _list[weight_i]


    printMatrix(matrix)


    return matrix

def printMatrix(matrix):
    for stuff in matrix:
        print(stuff)

def doBFS(startNode, endNode, matrix):
    print("Starting BFS from " + str(startNode) + " to " + str(endNode))
    for i, weight in enumerate(matrix[startNode]):
        if int(weight) > 0:
            print (startNode, ' is connected to ', i)

    
main()
    
