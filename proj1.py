#CS471
#Proj 1 - BFS, DFS, UCS
#Paolo Frias
#Due: 02/17/1992

import sys


def main():
    CONST_OFFSET = 64
    ######
    sys.argv = [sys.argv[0], 'inputTextFile.txt', 'Depth', 'L', 'G', 'outputFile.txt']
    ######

    startNode = ord(sys.argv[3]) - CONST_OFFSET - 1
    endNode = ord(sys.argv[4]) - CONST_OFFSET - 1
    masterList = list()
    
    #Input redirection
    file = open(sys.argv[1], "r")
    for line in file:
        for word in line.split(" "):
            masterList.append(word.rstrip())

    file.close()
    matrix = createMatrix(masterList)

    if sys.argv[2] == 'Breadth':
        path = doBFS(startNode, endNode, matrix)
    elif sys.argv[2] == 'Depth':
        parents = [startNode]
        visited = [False for i in range(len(matrix[0]))]
        path = doDFS(startNode, endNode, matrix, parents, visited)
    else:
        parents = [startNode]
        visited = [False for i in range(len(matrix[0]))]
        path = doUCS(startNode, endNode, matrix)

    outputFile = open("outputTextFile.txt", "w")
    for node in path:
        #print(chr(node + CONST_OFFSET + 1))
        outputFile.write(chr(node + CONST_OFFSET + 1) + "\n")

    outputFile.close()
    return 0

            
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


    #printMatrix(matrix)


    return matrix


def printMatrix(matrix):
    for stuff in matrix:
        print(stuff)


def doBFS(startNode, endNode, matrix):
    
    parent = [None for i in range(len(matrix[0]))]
    visited = [False for i in range(len(matrix[0]))]
    queue = []
    queue.append(startNode)
    
    while not allTrue(visited) and len(queue) != 0:
        currNode = queue[0]
        visited[currNode] = True
        for i, weight in enumerate(matrix[currNode]):
            if visited[i] == False and i not in queue:
                if int(weight) > 0:
                    parent[i] = currNode
                    queue.append(i)

        queue.pop(0)

    path = []        
    return getPath(startNode, endNode, parent, path)
                

def allTrue(_list):
    for i in _list:
        if i == False:
            return False
    return True


def getPath(startNode, endNode, parent, path):
    if endNode == startNode:
        path.append(startNode)
        path.reverse()
        return path
    else:
        path.append(endNode)
        endNode = parent[endNode]
        return getPath(startNode, endNode, parent, path)


def doDFS(startNode, endNode, matrix, parents, visited):
    visited[startNode] = True
    
    if endNode == startNode:
        return parents

    else:
        vertices = []
        for i, weight in enumerate (matrix[startNode]):
            if int(weight) > 0 and not visited[i] == True:
                vertices.append(i)

        if len(vertices) == 0:
            #This node has no more unvisited connections
            parents.pop()
            startNode = parents[-1]
            return doDFS(startNode, endNode, matrix, parents, visited)
            
        else:
            vertices.sort()
            startNode = vertices[-1]
            parents.append(startNode)
            return doDFS(startNode, endNode, matrix, parents, visited)


def doUCS(startNode, endNode, matrix):
    parent = [None for i in range(len(matrix[0]))]
    known = [False for i in range(len(matrix[0]))]
    cost = [None for i in range(len(matrix[0]))]

    currNode = startNode
    cost[startNode] = 0

    while not known[endNode] == True:
        known[currNode] = True
        for i, weight in enumerate(matrix[currNode]):
            if int(weight) > 0:
                nodeCost = cost[currNode] + int(weight)
                if (cost[i] == None or nodeCost < cost[i]):
                    parent[i] = currNode
                    cost[i] = nodeCost

        lowestIndex = None
        lowestCost = None
        for i, value in enumerate(cost):
            if not i == startNode and not value == None and not known[i] == True:
                if lowestIndex == None or value < lowestCost:
                    lowestIndex = i
                    lowestCost = value

        currNode = lowestIndex

    path = []
    return getPath(startNode, endNode, parent, path)

#####################    
main()
    
