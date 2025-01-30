from typing import List


from bisect import bisect_left, bisect_right

def max_coverage(cities, d, n):
    results = [0] * (n + 1)
    max_coverage = 0

    for i in range(n):
        left_bound = bisect_left(cities, cities[i] - d)
        right_bound = bisect_right(cities, cities[i] + d) - 1
        coverage = right_bound - left_bound + 1

        results[i] = coverage
        max_coverage = max(max_coverage, coverage)

    left = 0
    for right in range(n):
        while cities[right] - cities[left] > 2 * d:
            left += 1
        max_coverage = max(max_coverage, right - left + 1)

    results[-1] = max_coverage
    return results

# Test Case
n = 4
d = 3
A = [1, 3, 5, 7]
print(max_coverage(A, d, n))  # Expected Output: [2, 3, 3, 2, 4]