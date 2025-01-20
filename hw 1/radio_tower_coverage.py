from typing import List
import sys

def radioTowerCoverage(n: int, d: int, A: List[int]) -> List[int]:
    right_endpoints = [0] * n
    r = 0
    for i in range(n):
        while r < n and A[r] - A[i] <= d:
            r += 1
        right_endpoints[i] = r - 1
    
    left_endpoints = [0] * n
    l = 0
    for i in range(n):
        while A[i] - A[l] > d:
            l += 1
        left_endpoints[i] = l

    results = []
    for i in range(n):
        coverage = right_endpoints[i] - left_endpoints[i] + 1
        results.append(coverage)

    max_coverage = 0
    l = 0
    for r in range(n):
        while A[r] - A[l] > 2 * d:
            l += 1
        max_coverage = max(max_coverage, r - l + 1)

    results.append(max_coverage)
    return results

input = sys.stdin.read().strip().split("\n")
n, d = map(int, input[0].split())
A = list(map(int, input[1].split()))
results = radioTowerCoverage(n, d, A)

print("\n".join(map(str, results)))