# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# 1. Use math formula to get. Total steps: m+n-2, choose n-1 steps to go down.
# Note: m = max(m, n); n = min(m, n)

# 2. DP. except first row and first column, others equals to the sum of above and previous elem.
# Time: O(mn)

class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        m, n = max(m, n), min(m, n)
        upper = 1
        lower = 1
        for elem in range(m, m+n-1):
            upper *= elem
        for elem in range(1, n):
            lower *= elem
        return upper // lower

    def uniquePaths2(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        res = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]