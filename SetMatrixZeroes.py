# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# 1. Brute force. 
# Time: O(N^2) Space: O(m+n)

# 2. Use the first row and col to record.
# Time: O(N^2) Space: O(1)

# 3. Use 'X' to represent those positions that should be 0
# Time: O(N^2) Space: O(1)


class Solution:
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in row) or (j in col):
                    matrix[i][j] = 0


    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        r, c = len(matrix), len(matrix[0])
        record = 1
        for i in range(c):
            if matrix[0][i] == 0:
                record = 0
                break
                
        for i in range(1, r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, r):
            if matrix[i][0] == 0:
                matrix[i] = [0] * c
        for j in range(c):
            if matrix[0][j] == 0:
                for i in range(1, r):
                    matrix[i][j] = 0
        if record == 0:
            matrix[0] = [0] * c

    def setZeroes3(self, matrix):
        if not matrix:
            return matrix
        h, w = len(matrix), len(matrix[0])
        for i in xrange(h):
            for j in xrange(w):
                if matrix[i][j] == 0:
                    for ii in xrange(h):
                        if matrix[ii][j] != 0:
                            matrix[ii][j] = 'x'
                    for jj in xrange(w):
                        if matrix[i][jj] != 0:
                            matrix[i][jj] = 'x'
        for i in xrange(h):
            for j in xrange(w):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0 