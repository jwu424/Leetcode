# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# 1. for level i, except for the first 1 and the last 1, other values can be generated basing on the upper level.
# Note: we should be careful when numRows = 0 or 1.
# Time complexity: O(N^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
     
        res = [[1]]
        for k in range(1, numRows):
            temp = [1]
            for i in range(len(res[-1])-1):
                temp.append(res[-1][i]+res[-1][i+1])
            res.append(temp+[1])
        return res