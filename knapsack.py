import copy
import sys

class KnapsackTreeNode:
    def __init__(self):
        self.sack = []
        self.candidates = []
        self.utility = 0
        self.weight = 0

    def optimal_estimation(self, sack_capacity):
        u = self.utility
        w = self.weight
        i = 0
        while w < sack_capacity and i < len(self.candidates):
            u += self.candidates[i].utility
            w += self.candidates[i].weight
            i += 1
        return (u, w, i-1)

class O:
    def __init__(self, index, utility, weight):
        self.index = index
        self.utility = utility
        self.weight = weight
    def __str__(self):
        return f"(u:{self.utility}, w:{self.weight})"

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
    node = fifo.pop(0)
    u, w, i = node.optimal_estimation(B)

    if w > B:
        o = node.candidates[i]
        u -= ((w-B) / o.weight) * o.utility
    
    if u > u_cour:
        if w <= B:
            u_cour = u
            w_cour = w
            sol_cour = node.sack.copy()
            sol_cour.extend(node.candidates[:i+1])
        else:
            splitter = node.candidates.pop(i)
            child1 = copy.copy(node)
            child1.sack.append(splitter)
            fifo.extend([child1, node])
print("Utility:", u_cour)
print("Weight:", w_cour)
print("Number of objects:", len(sol_cour))
print("Sack: ", end="")
for o in sol_cour:
    print(o.index, sep=", ", end=" ")
print("\n")
