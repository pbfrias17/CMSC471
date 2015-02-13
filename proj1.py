#CS471
#Proj 1 - BFS, DFS, UCS
#Paolo Frias
#Due: 02/17/1992


def main():
    masterList = list()
    
    #Input redirection
    file = open("inputTextFile.txt", "r")
    for line in file:
        for word in line.split(" "):
            masterList.append(word.rstrip())

    matrix = createMatrix(masterList)

    #Breadth First Search
    
            
def createMatrix(_list):
    largest = 0
    CONST_OFFSET = 64
    
    #create graph matrix
    for i in _list:
        if len(i) <= 1:
            if ord(i) > 64 and ord(i) < 90:
                i = ord(i) - CONST_OFFSET
                if largest < i:
                    largest = i

    print(largest)
    matrix = [[0 for x in range(largest)] for y in range(largest)]

    #fill matrix
    itr = 0
    while itr < len(_list):
    printMatrix(matrix)


    return matrix

def printMatrix(matrix):
    for stuff in matrix:
        print(stuff)
    

    
main()
    
