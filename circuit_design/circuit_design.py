# python3
import sys
import threading

sys.setrecursionlimit(10**7)  # max recursion limit
#threading.stack_size(2**62)  # max stack size
threading.stack_size(2**30)  # max stack size

#--------------------------------------------------------
# My own SSC counter from earlier Coursera unit.
#--------------------------------------------------------
def explore(adj,v,component_list,component_number):
    component_list[v] = component_number
    for w in adj[v]:
        if component_list[w] == 0:
            explore(adj,w,component_list,component_number)

def dfs(adj,v,visited,pre,post,tic):
    visited[v] = True
    tic[0] += 1
    pre[v] = tic[0]
    for w in adj[v]:
        if not visited[w]:
            dfs(adj,w,visited,pre,post,tic)
    tic[0] += 1
    post[v] = tic[0]

def dfs_it(adj, vin, visited, pre, post):
    tic = 0
    queue = [vin]
    post_queue = []
    while queue:
        v = queue.pop()
        post_queue.append(v)
        tic += 1
        pre[v] = tic
        visited[v] = True
        queue.extend(adj[v])
        print(pre)
    while post_queue:
        v = post_queue.pop()
        tic += 1
        post[v] = tic

def toposort(adj):
    tic = [0]
    visited = [False for i in range(len(adj))]
    pre = [-1 for i in range(len(adj))]
    post = [-1 for i in range(len(adj))]
    for v in range(len(adj)):
        if visited[v] == False:
            dfs(adj,v,visited,pre,post,tic)
            #dfs_it(adj,v,visited,pre,post)
    #print("pre:  ", pre)
    #print("post: ", post)
    order = list(range(len(post)))
    return sorted(order,key=lambda x: post[x],reverse=True)

def number_of_strongly_connected_components(adj,adr):
    rpost_order = toposort(adr)
    component_list = [0 for i in range(len(adr))]
    component_number = 0
    for v in rpost_order:
        if component_list[v] == 0:
            component_number += 1
            explore(adj,v,component_list,component_number)
    return component_number, component_list, rpost_order
#------------------------------------------------------------
#------------------------------------------------------------

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable_naive():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def sign(x):
    if x<0:
        return -1
    return 1

def node(x):
    if x > 0:
        return 2*(x-1)
    else:
        return 2*(abs(x)-1)+1

def not_node(x):
    if x < 0:
        return 2*(abs(x)-1)
    else:
        return 2*(x-1)+1

# n variables
# m clauses
def isSatisfiable(n,m,clauses):
    impgr = [[] for _ in range(2*n)]
    rimpgr = [[] for _ in range(2*n)]
    #for each variable x_i, its node is 2*i and its negation is 2*i+1
    # i ranges from 0 to n-1
    for clause in clauses:
        #print('clause is: ',clause)
        #print('first implication is: ',not_node(clause[0]),node(clause[1]))
        #print('secon implication is: ',not_node(clause[1]),node(clause[0]))
        #make implication graph
        impgr[not_node(clause[0])].append(node(clause[1]))  #node not a points to node b
        impgr[not_node(clause[1])].append(node(clause[0]))  #node not a points to node b
        #make reversed implication graph, for SSC finder
        rimpgr[node(clause[1])].append(not_node(clause[0]))  #node not a points to node b
        rimpgr[node(clause[0])].append(not_node(clause[1]))  #node not a points to node b
        #There are only 2-clauses in the problem, no 1-clauses
    #print(impgr)
    nssc, ssclst, rpost_order = number_of_strongly_connected_components(impgr,rimpgr)
    #print('ssclst: ', ssclst)
    for i in range(n):
        if ssclst[2*i] == ssclst[2*i+1]:
            return  None
    #print('rpost_order:', rpost_order)
    assignment = [None for _ in range(2*n)]
    for vertex in rpost_order:
        if assignment[vertex] == None:
            assignment[vertex] = 1
            if vertex%2 == 0:
                assignment[vertex+1] = 0
            else:
                assignment[vertex-1] = 0
    result = [i if assignment[2*(i-1)] else -i for i in range(1,n+1)]
    return result


def main():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    #with open('sample1.input','r') as f:
    #    n,m = map(int, f.readline().split())
    #    clauses = []
    #    for line in f:
    #        #print(line.split())
    #        clauses.append(list(map(int,line.split())))
    #result = isSatisfiable_naive()
    result = isSatisfiable(n,m,clauses)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join([str(x) for x in result]))

threading.Thread(target=main).start()
#main()

