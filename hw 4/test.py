def compute_min_radius(P, A, k):
    # scale A by 60 to avoid float issues
    A = [a * 60 for a in A]
    n = len(A)
    
    # set binary search range for q = 60*d
    # worst-case: need to cover gap A[-1]-A[0] with the smallest P value
    right = (A[-1] - A[0]) * 100 // min(P)
    left = 0
    
    def can_cover(q):
        # for each city i, tower placed there covers:
        # [A[i] - (q * P[i])//100, A[i] + (q * P[i])//100]
        intervals = []
        for i in range(n):
            L = A[i] - (q * P[i]) // 100
            R = A[i] + (q * P[i]) // 100
            intervals.append((L, R))
        # sort intervals by starting point
        intervals.sort(key=lambda x: x[0])
        
        used = 0  # number of towers used
        i = 0      # index for cities
        j = 0      # index for intervals (sorted)
        while i < n:
            best = -1
            # choose the interval with the farthest right endpoint among those that start <= A[i]
            while j < n and intervals[j][0] <= A[i]:
                best = max(best, intervals[j][1])
                j += 1
            if best < A[i]:
                return False  # no interval covers A[i]
            used += 1
            # skip all cities covered by the chosen interval
            while i < n and A[i] <= best:
                i += 1
            if used > k:
                return False
        return True
    
    while left < right:
        mid = (left + right) // 2
        if can_cover(mid):
            right = mid
        else:
            left = mid + 1

    return left  # left is q = 60*d


# read test cases from testcases.txt
with open("testcases.txt", "r") as f:
    lines = f.read().strip().split("\n")

tc = int(lines[0])
index = 1
results = []

for _ in range(tc):
    n, k = map(int, lines[index].split())
    P = list(map(int, lines[index + 1].split()))
    A = list(map(int, lines[index + 2].split()))
    index += 3
    # our function returns q = 60*d, so we print it directly
    results.append(str(compute_min_radius(P, A, k)))

# print results, one per line
print("\n".join(results))