# python3
from itertools import combinations, permutations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def StoSint(S,n):
    result = 0
    for s in S:
        result += 2**s
    return result

def SintRemove(Sint,j):
    return Sint ^ (1 << j)

def optimal_path(graph):
    n = len(graph)
    C = {(1,0):0}
    P = {(1,0):()}
    for s in range(2,n+1):
        for S in combinations(range(1,n),s-1):
            S = S + (0,)
            Sint = StoSint(S,n)
            C[(Sint,0)] = INF
            P[(Sint,0)] = ()
            for i in S[:-1]:  #element 0 is always at end
                C[(Sint,i)] = INF
                P[(Sint,i)] = (-1,)
                for j in S:
                    if j != i:
                        if C[(SintRemove(Sint,i),j)]+graph[i][j] < C[(Sint,i)]:
                            C[(Sint,i)] = C[(SintRemove(Sint,i),j)]+graph[i][j] 
                            P[(Sint,i)] = P[(SintRemove(Sint,i),j)] + (j,)


    fullset = 2**n-1
    result = [ C[(fullset,i)] + graph[i][0] for i in range(n) ]
    ans = min(result)
    if ans < INF:
        bestix = result.index(ans)
        bestpath = P[(fullset,bestix)] + (bestix,)
    else:
        ans = -1
        bestpath = [-1]
    return ans, [p+1 for p in bestpath]

def optimal_path_niave(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


if __name__ == '__main__':
    #print_answer(*optimal_path_niave(read_data()))
    print_answer(*optimal_path(read_data()))

