# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# 1. Use zip to transform the matrix. 
# The meaning of return a and b is that when a is empty, the function jumps out. When a is not empty, b is executed. I am confused about this.
# Time: 
# T(m, n) = O(n) + O((n-1)*m) + T(n-1, m); 
# O(n) to extend and O((n-1)*m) to rotate.
# O(n) + O((n-1)*m) is around O(mn)
# T(m, n) = O(mn)+T(n-1,m) = O(2mn)+T(n-1, m-1)
# T(m, n) = O(min(m,n)*mn)

# 2. Normal way.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while l < r and u < d:
            ans.extend([matrix[u][j] for j in range(l, r)])
            ans.extend([matrix[j][r] for j in range(u, d)])
            ans.extend([matrix[d][j] for j in range(r, l, -1)])
            ans.extend([matrix[j][l] for j in range(d, u, -1)])
            u, d, l, r = u+1, d-1, l+1, r-1
        if l == r:
            ans.extend([matrix[j][r] for j in range(u, d+1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in range(l, r+1)])
        return ans