#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

OPTPRINT = 0
def optprint(*args):
    if OPTPRINT:
        print(*args)

class Vertex:
    def __init__(self, weight, name):
        self.name = name # helps debugging
        self.weight = weight
        self.children = []
        self.D = None  # maximum weight of independent set descendants

def ReadTree():
    size = int(input())
    tree = [Vertex(w,ix+1) for ix,w in enumerate(map(int, input().split()))]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def dfs(tree, vertex, parent):
    if tree[vertex].D == None:
        optprint()
        optprint('name: ',tree[vertex].name)
        optprint('weight: ',tree[vertex].weight)
        optprint('parent name: ',parent+1)
        optprint('children: ',[x+1 for x in tree[vertex].children])
        if len(tree[vertex].children) > 1 or vertex == 0:
            optprint('has children')
            m1 = tree[vertex].weight
            for child_u in tree[vertex].children:
                if child_u != parent:
                    optprint('child_u, parent: ', child_u+1, parent+1)
                    for child_w in tree[child_u].children:
                        optprint('child_w, vertex', child_w+1, vertex+1)
                        if child_w != vertex:
                            optprint('vertex dfs(child_w, child_u): ', vertex+1, 'dfs(',child_w+1, child_u+1,')')
                            m1 = m1 + dfs(tree, child_w, child_u)
            m0 = 0
            for child_u in tree[vertex].children:
                if child_u != parent:
                    m0 = m0 + dfs(tree,child_u,vertex)
            tree[vertex].D = max(m0,m1)
        else:
            optprint('stump out: ', vertex+1)
            tree[vertex].D = tree[vertex].weight
    return tree[vertex].D
    
def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    return dfs(tree, 0, -1)

def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
#main()
