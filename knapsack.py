import copy
import sys

class KnapsackTreeNode:
    def __init__(self):
        self.sack = []
        self.candidates = []
        self.utility = 0
        self.weight = 0
        self.parent_estimation = 0

    def copy(self):
        node = KnapsackTreeNode()
        node.sack.extend(self.sack)
        node.candidates.extend(self.candidates)
        node.utility = self.utility
        node.weight = self.weight

        return node

    def optimal_estimation(self, sack_capacity):
        u = self.utility
        w = self.weight
        i = 0
        while w < sack_capacity and i < len(self.candidates):
            u += self.candidates[i].utility
            w += self.candidates[i].weight
            i += 1
        if w > sack_capacity and i > 0:
            u -= ((w-sack_capacity)/self.candidates[i-1].weight)*self.candidates[i-1].utility
            return (int(u), w, i-1)
        else:
            return (int(u), w, -1)
            
    def print_sack(self, sack):
        string=""
        for o in sack:
            string += str(o)+", "
        return string

    def __str__(self):
    	return f"U:{self.utility}\nW:{self.weight}\nCandidate:{self.print_sack(self.candidates)}\nSack:{self.print_sack(self.sack)}"

class O:
    def __init__(self, index, utility, weight):
        self.index = index
        self.utility = utility
        self.weight = weight
    def __str__(self):
        return f"(i:{self.index}, u:{self.utility}, w:{self.weight})"

def compute_initial_solution(sack, candidates, sack_capacity):
    w, u = 0, 0
    sack = sack.copy()
    for o in candidates:
        if o.weight + w <= sack_capacity:
            sack.append(o)
            u += o.utility
            w += o.weight
    return sack, u, w

def read_input(fname):
    with open(fname) as f:
        N, B = list(map(lambda x: int(x), f.readline().split(" ")))
        objects = []
        i = 1
        for line in f:
            u, w = list(map(lambda x: int(x), line.split(" ")))
            objects.append(O(index=i, utility=u, weight=w))
            i+=1
    return objects, B

##B = 20 # capacity of the sack
##
##objects = [O(10, 7), O(12, 10), O(7, 3), O(13, 5), O(4, 6), O(5, 4), O(3, 2)]

if len(sys.argv) < 2:
    print("Syntax error\n Usage: python snapsack.py [input_file]")
    exit(-1)

objects, B = read_input(sys.argv[1])

objects.sort(key=lambda o: o.utility/o.weight,  reverse=True)

sol_cour, u_cour, w_cour = compute_initial_solution([], objects, B)

root = KnapsackTreeNode()
root.sack = []
root.candidates.extend(objects)

fifo = [root]

it = 0
while len(fifo) > 0:
    it += 1
    node = fifo[0]
    u, w, i = node.optimal_estimation(B)
    # print(f"node-{it}\n{node}\n\nu={u}, u_cour={u_cour}\nw={w}, w_cour={w_cour}\ni=",i)

    if u <= u_cour:
        fifo.pop(0)
    else:
        if w <= B:
            u_cour = u
            w_cour = w
            sol_cour = node.sack.copy()
            if i == -1:
                sol_cour.extend(node.candidates)
            else:
                sol_cour.extend(node.candidates[:i])
        else:
            splitter = node.candidates.pop(i)
            child1 = node.copy()
            child1.utility += splitter.utility
            child1.weight += splitter.weight
            child1.sack.append(splitter)
            child1.parent_estimation = u
            child2 = node.copy()
            child2.parent_estimation = u
            fifo.append(child2)
            # print("child1", child1, "\n", "child2", child2, "\n\n")
            if child1.weight < B:
                fifo.append(child1)
        fifo.pop(0)
    # input("go...\n")
print("Utility:", u_cour)
print("Weight:", w_cour)
print("Number of objects:", len(sol_cour))
print("Sack: ", end="")
for o in sol_cour:
    print(o.index, sep=", ", end=" ")
print("\n")
