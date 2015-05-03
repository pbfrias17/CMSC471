import math

class DecisionTree:
    training_set = []
    tree = [[], []]

    def init_tree(self, tree, depth):
        if depth == (len(self.training_set[0]) - 2):
            tree[0] = None
            tree[1] = None
        else:
            for i in range(len(tree)):
                tree[i] = [[], []]
                self.init_tree(tree[i], depth + 1)

    def descend(self, tree, path, leaf):
        if len(path) == 1:
            index = path[0]
            if leaf is None:
                return tree[index]
            else:
                tree.insert(index, leaf)
                tree.pop(index + 1)
        else:
            branch = path.pop(0)
            return self.descend(tree[branch], path, leaf)

    def train(self, data_set):
        self.training_set = list(data_set)
        self.init_tree(self.tree, 0)
        for vector in self.training_set:
            leaf = vector.pop(0)
            self.descend(self.tree, vector, leaf)

        print(data_set)
        print(self.training_set)

    def classify(self, data_set):
        return self.descend(self.tree, data_set, None)


class NaiveBayes:
    def train(self, training_set):
        #what features of the vector should we consider?

        self.amount_of_ones = 0
        self.total = 0
        for vector in training_set:
            self.total += 1
            self.amount_of_ones += vector[0]
        print(self.amount_of_ones)

        self.prob_one = self.amount_of_ones / self.total

        #We will consider the amount of 1(s) in each vector
        
        self.ones_in_each = []
        for vector in training_set:
            ones = 0
            for i in range(1, len(vector)):
                ones += vector[i]
            self.ones_in_each.append(ones)

        print(self.ones_in_each)
                
                
                
    

class NearestNbr:
    
    def train(self, training_set):
        self.neighbors = training_set

    def classify(self, data_set):
        nearest_dist = -1
        for i in range(len(self.neighbors)):
            dist = self.distance(data_set, i)
            if nearest_dist < 0 or dist < nearest_dist:
                nearest_dist = dist
                nearest_index = i

        return self.neighbors[nearest_index][0]

    def distance(self, data_set, index):
        sum = 0
        for i in range(len(data_set)):
            sum += pow(data_set[i] - (self.neighbors[index][i+1]), 2)

        return math.sqrt(sum)
            


def main():

    test_set = []
    f = open("test_sets.txt", 'r')
    for line in f:
        stringed_list = line.split()
        numbered_list = []
        for var in line.split():
            numbered_list.append(ord(var) - 48)
        test_set.append(numbered_list)
    print(test_set)

    print("NAIVE BAYES:")
    NB = NaiveBayes()
    NB.train(test_set)
    print()

    print("NEAREST NEIGHBOR")
    NN = NearestNbr()
    NN.train(test_set)
    print("'000' classified as: ", NN.classify([0, 0, 0]))
    print()

    #for some reason, couldn't get my train method to pass in the test_set
    # by value. DT must be last since it changes the test_set
    print("DECISION TREE")
    DT = DecisionTree()
    DT.train(test_set)
    print("deciding... ", DT.classify([1, 0, 1]))

    return 0

main()
