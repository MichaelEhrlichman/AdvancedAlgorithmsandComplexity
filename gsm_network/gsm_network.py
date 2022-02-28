# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

TRAILING_ZERO = ''

def printEquisatisfiableSatFormula():
    print('{} {}'.format(4*n+3*len(edges), 3*(n-1)+3))
    for i in range(n):
        #Each node must have one and only one color
        print('{} {} {} {}'.format( 3*i+1, 3*i+2, 3*i+3, TRAILING_ZERO ))
        print('{} {} {}'.format( -(3*i+1), -(3*i+2), TRAILING_ZERO ))
        print('{} {} {}'.format( -(3*i+1), -(3*i+3), TRAILING_ZERO ))
        print('{} {} {}'.format( -(3*i+2), -(3*i+3), TRAILING_ZERO ))
    for a,b in edges:
        #Each edge must have a different color on each end
        print('{} {} {}'.format( -(3*(a-1)+1), -(3*(b-1)+1), TRAILING_ZERO ))
        print('{} {} {}'.format( -(3*(a-1)+2), -(3*(b-1)+2), TRAILING_ZERO ))
        print('{} {} {}'.format( -(3*(a-1)+3), -(3*(b-1)+3), TRAILING_ZERO ))

printEquisatisfiableSatFormula()
