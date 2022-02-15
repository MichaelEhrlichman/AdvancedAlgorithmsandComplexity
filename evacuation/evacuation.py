# python3
from collections import deque


class Edge:

  def __init__(self, u, v, capacity):
    self.u = u
    self.v = v
    self.capacity = capacity
    self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

  def __init__(self, n):
    # List of all - forward and backward - edges
    self.edges = []
    # These adjacency lists store only indices of edges in the edges list
    self.graph = [[] for _ in range(n)]

  def add_edge(self, from_, to, capacity):
    # Note that we first append a forward edge and then a backward edge,
    # so all forward edges are stored at even indices (starting from 0),
    # whereas backward edges are stored at odd indices.
    forward_edge = Edge(from_, to, capacity)
    backward_edge = Edge(to, from_, 0)
    self.graph[from_].append(len(self.edges))
    self.edges.append(forward_edge)
    self.graph[to].append(len(self.edges))
    self.edges.append(backward_edge)

  def size(self):
    return len(self.graph)

  def get_ids(self, from_):
    return self.graph[from_]

  def get_edge(self, id):
    return self.edges[id]

  def add_flow(self, id, flow):
    # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
    # due to the described above scheme. On the other hand, when we have to get a "backward"
    # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
    # should be taken.
    #
    # It turns out that id ^ 1 works for both cases. Think this through!
    self.edges[id].flow += flow
    self.edges[id ^ 1].flow -= flow

  def saturated(self,edgeid):
    return self.edges[edgeid].flow == self.edges[edgeid].capacity

def even(num):
  return num%2==0

def edmonds_karp_BFS(graph):
  explored = [False for _ in range(graph.size())]
  parents = [None for _ in range(graph.size())]
  stack = deque([0])
  while stack:
    nodeid = stack.pop()
    explored[nodeid] = True
    for edgeid in graph.graph[nodeid]:
      if even(edgeid) and not graph.saturated(edgeid):  # if even
        v_node = graph.get_edge(edgeid).v
        u_node = graph.get_edge(edgeid).u
        if not explored[v_node]:
          stack.appendleft(v_node)
          parents[v_node] = u_node
          print(u_node, v_node, graph.get_edge(edgeid).capacity)
          if v_node == len(graph.graph)-1:
            # found the sink
            print('sink!')
            path_node = v_node
            path = [path_node]
            while True:
              path.append(parents[path_node])
              path_node = parents[path_node]
              if(path_node == 0):
                return(path)


def read_data():
  vertex_count, edge_count = map(int, input().split())
  graph = FlowGraph(vertex_count)
  for _ in range(edge_count):
    u, v, capacity = map(int, input().split())
    graph.add_edge(u - 1, v - 1, capacity)
  return graph

def read_data_file(filename):
  with open(filename,'r') as f:
    vertex_count, edge_count = map(int, f.readline().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
      u, v, capacity = map(int, f.readline().split())
      graph.add_edge(u-1, v-1, capacity)
  return graph

def max_flow(graph, from_, to):
  flow = 0
  # your code goes here
  print(edmonds_karp_BFS(graph))
  #graph.edges[0].flow = 2
  #print(edmonds_karp_BFS(graph))
  return flow


if __name__ == '__main__':
  #graph = read_data()
  graph = read_data_file("tests/01")
  print(max_flow(graph, 0, graph.size() - 1))
