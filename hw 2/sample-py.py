from collections import deque


def compute_diameter(n, edges):
    # Input: `n` - the size of the tree
    # `edges` - a list of pairs of integers denoting ends of edges of the tree
    # Output: An integer - the diameter of the tree
    adj = [[] for _ in range(n+1)]  # 1-based indexing for nodes
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    diameter = 0

    def bfs(start):
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        farthest_node = start
        max_distance = 0

        while queue:
            u, dist = queue.popleft()
            if dist > max_distance:
                max_distance = dist
                farthest_node = u
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, dist + 1))

        return farthest_node, max_distance
        
    start_node = 1
    farthest_from_start, _ = bfs(start_node)
    _, diameter = bfs(farthest_from_start)

    return diameter


T = int(input())
for _ in range(T):
    n = int(input())
    edges = []
    for e in range(n-1):
        u, v  = map(int, input().split(' '))
        edges.append((u, v))
    print(compute_diameter(n, edges))