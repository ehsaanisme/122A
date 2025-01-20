from typing import List

def solve_radio_coverage(n: int, d: int, cities: List[int]) -> List[int]:
    dp = [0] * n  # dp[i] stores coverage for a tower placed at A[i]
    left = 0

    # Step 1: Calculate dp[i] for city-specific coverage
    for i in range(n):
        while cities[i] - cities[left] > d:
            left += 1
        dp[i] = i - left + 1

    # Step 2: Calculate maximum arbitrary placement
    left = 0
    max_coverage = 0
    for i in range(n):
        while cities[i] - cities[left] > 2 * d:
            left += 1
        max_coverage = max(max_coverage, i - left + 1)

    # Step 3: Combine results
    result = dp + [max_coverage]
    return result

# Test Case
n = 4
d = 3
A = [1, 3, 5, 7]
print(solve_radio_coverage(n, d, A))  # Expected Output: [2, 3, 3, 2, 4]