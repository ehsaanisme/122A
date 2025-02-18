''' Complete the following function:
    Given the weights of vertices and edges of the graph, compute the minimum cost
    weights[i] = weight of vertex i (ignore weights[0])
    The i^{th} edge (0-indexed) is between (edges[i].u, edges[i].v) and has weight edges[i].w
    edges is a vector of size m, (i.e., the edges are described by edges[0], edges[1], ... edges[m-1])
'''

from heapq import heappush, heappop

# inspired from neetcode.io

class UnionFind:
    def __init__(self, n):
        # here we set up the union find structure
        self.parent = list(range(n + 1))  # 1-based indexing
        self.rank = [0] * (n + 1)

    def find(self, u):
        # here we find the root parent with path compression
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # here we merge two sets if they are not already connected
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True

def computeMinimumCost(weights, edges):
    n = len(weights) - 1  # number of villages
    minHeap = []
    
    # here we add all road edges to the heap
    for u, v, w in edges:
        heappush(minHeap, (w, u, v))

    # here we add virtual edges from a fake node (0) to each village with a well
    for i in range(1, n + 1):
        if weights[i] != -1:
            heappush(minHeap, (weights[i], 0, i))  

    dsu = UnionFind(n)
    total_cost = 0
    edges_used = 0

    # here we build the minimum spanning tree (mst)
    while minHeap and edges_used < n:
        cost, u, v = heappop(minHeap)
        if dsu.union(u, v):  # only add if it connects new components
            total_cost += cost
            edges_used += 1

    return total_cost

# The following lines take care of input and output for you. You may ignore this section.

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    weights = list(map(int, ("0 " + input()).split())) # Adding 0 to index weights by 1, instead of 0
    edges = []
    for _ in range(m):
        u, v, w  = map(int, input().split(' '))
        edges.append((u, v, w))
    print(computeMinimumCost(weights, edges))
