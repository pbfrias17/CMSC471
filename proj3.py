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

    def classify(self, data_set):
        return self.descend(self.tree, data_set, None)


class NaiveBayes:
    
    def train(self, training_set):
        self.training_set = training_set
        self.amount_of_ones = 0
        self.total = 0
        for vector in training_set:
            self.total += 1
            self.amount_of_ones += vector[0]

        self.prob_one = self.amount_of_ones / self.total

        #We will consider the amount of 1(s) in each vector
        self.ones_in_each = []
        for vector in training_set:
            ones = 0
            for i in range(1, len(vector)):
                ones += vector[i]
            self.ones_in_each.append(ones)
        
    def classify(self, data_set):
        ones = 0
        for var in data_set:
            ones += var

        #P(data_set is 1 | data_set has x 1s)
        total_ones = 0
        total_amount = 0
        for i in range(len(self.ones_in_each)):
            if self.ones_in_each[i] == ones:
                total_ones += self.training_set[i][0]
                total_amount += 1
                
        prob = total_ones / total_amount
        if prob >= .5:
            return 1

        return 0

                
                
    

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

    data_set_list = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 0, 0]]

    print("NAIVE BAYES:")
    NB = NaiveBayes()
    NB.train(test_set)
    for data_set in data_set_list:
        print(data_set, "classified as", NB.classify(data_set))
    print()

    print("NEAREST NEIGHBOR")
    NN = NearestNbr()
    NN.train(test_set)
    for data_set in data_set_list:
        print(data_set, "classified as", NN.classify(data_set))
    print()

    #for some reason, couldn't get my train method to pass in the test_set
    # by value. DT must be last since it changes the test_set
    print("DECISION TREE")
    DT = DecisionTree()
    DT.train(test_set)
    for data_set in data_set_list:
        clone_set = data_set[:]
        print(clone_set, "classified as", DT.classify(data_set))

    return 0

main()
