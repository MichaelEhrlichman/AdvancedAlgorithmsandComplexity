# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

TRAILING_ZERO = ' 0'
DEBUG = 0

def encode(i,j):
    # x_i,j where i is node number, and j is path location
    # encode indexes to single subscript
    return (i-1)*n+j

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    output = []
    counter = 0
    # Each vertex belongs to the path
    if DEBUG:
        output.append('# Each vertex belongs to the path')
    for i in range(n):
        counter += 1
        output.append(' '.join([str(encode(i+1,j+1)) for j in range(n)]))

    # Each vertex appears only once in the path
    if DEBUG:
        output.append('# Each vertex appears only once in the path')
    for i in range(1,n+1):  #over nodes
        for j in range(1,n):  #over paths
            for k in range(j+1,n+1):
                counter += 1
                output.append('{} {}'.format(-encode(i,j),-encode(i,k)))

    # Each position in the path is occupied by a vertex
    if DEBUG:
        output.append('# Each position in the path is occupied by a vertex')
    for i in range(n):
        counter += 1
        output.append(' '.join([str(n*j+i+1) for j in range(n)]))

    ## Two vertices on a path cannot be successive unless connected by an edge
    #for i in range(1,n):  # node i
    #    for j in range(1,n):  # path j
    #        a = encode(i,j)
    #        for k in range(i+1,n+1):  # connecting node k
    #            #print("i,j,k: ",i,j,k)
    #            b = encode(k, j+1)
    #            if [i,k] in edges: 
    #                pass
    #            else:
    #                output.append('{} {}'.format(-a,-b))
    #                counter += 1

    # Each position in the path appears only once
    if DEBUG:
        output.append('# Each position in the path appears only once')
    for i in range(1,n+1):  #over path
        for j in range(1,n+1):  #over first vertex
            for k in range(j+1,n+1):  #over second vertex
                counter += 1
                output.append('{} {}'.format(-encode(j,i),-encode(k,i)))

    # Vertices not connected by an edge cannot be consecutive in the path
    if DEBUG:
        output.append('# Vertices not connected by an edge cannot be consecutive in the path')
    for i in range(1,n):  #over first vertex
        for j in range(i+1,n+1):  #over second vertex
            if [i,j] not in edges and [j,i] not in edges:
                for k in range(1,n):
                    counter += 2
                    output.append('{} {}'.format(-encode(i,k),-encode(j,k+1)))
                    output.append('{} {}'.format(-encode(i,k+1),-encode(j,k)))

    print('{} {}'.format(counter, n*n))
    for line in output:
        print(line+TRAILING_ZERO)

printEquisatisfiableSatFormula()
