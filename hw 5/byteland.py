'''
gotta find the shortest time to reach every cell. bfs isn't gonna work since different cells have different weights, so dijkstra with a min-heap makes sense.   

need a way to track teleports efficiently, so maybe preprocess all their positions into lists? like store row-wise and column-wise teleport locations so we can just jump to the farthest one instantly.  

spiky cells are tricky since ada can only step on a limited number. gotta keep track of how many she's used so far in the state we push into the heap.  

each state in the priority queue should be (time, row, col, spikes_used). once we pop a cell, we check all four directions and push valid moves into the heap. also, if it's a teleport cell, just jump straight to the farthest one in its row or column.  

gotta handle unreachable cells by keeping them at -1. if a cell is rocky, just skip it entirely. print the grid as the output.
'''
import sys
import heapq

def find_teleports(R, C, grid):
    # we get the teleport cell locations for quick access during pathfinding
    teleport_rows = [[] for _ in range(C)]
    teleport_cols = [[] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == -1:
                teleport_rows[c].append(r)
                teleport_cols[r].append(c)

    return teleport_rows, teleport_cols

def dijkstra(R, C, H, grid, teleport_rows, teleport_cols):
    # we use Dijkstra's algorithm and priority queue to find the shortest travel times
    # not bfs\

    result = [[-1 for _ in range(C)] for _ in range(R)]
    pq = [(0, 0, 0, 0)]
    visited = set()

    while pq:
        time, r, c, spikes = heapq.heappop(pq)

        if (r, c, spikes) in visited:
            continue
        visited.add((r, c, spikes))
        result[r][c] = time

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == 0:
                    continue  # skip here
                cost = 1 if grid[nr][nc] == 1 or grid[nr][nc] == -2 else grid[nr][nc]
                new_spikes = spikes + (1 if grid[nr][nc] == -2 else 0)
                if new_spikes <= H and (nr, nc, new_spikes) not in visited:
                    heapq.heappush(pq, (time + cost, nr, nc, new_spikes))

        if grid[r][c] == -1:
            if teleport_rows[c]:
                heapq.heappush(pq, (time + 1, teleport_rows[c][-1], c, spikes))
                heapq.heappush(pq, (time + 1, teleport_rows[c][0], c, spikes))

            if teleport_cols[r]:
                heapq.heappush(pq, (time + 1, r, teleport_cols[r][-1], spikes))
                heapq.heappush(pq, (time + 1, r, teleport_cols[r][0], spikes))

    return result

def byteland(R, C, H, grid):
    # finds the shortest path matrix using Dijkstra's algorithm with teleportation
    teleport_rows, teleport_cols = find_teleports(R, C, grid)
    return dijkstra(R, C, H, grid, teleport_rows, teleport_cols)

T = int(input())
for _ in range(T):
    R, C, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    result = byteland(R, C, H, grid)

    for row in result:
        print(*row, sep=' ')