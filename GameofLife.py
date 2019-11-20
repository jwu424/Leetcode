# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

# 1. Not in place. fist calculate the neighboor of each elem in board. And then apply the rule.
# Time complexity: O(N^2)

# 2. In place. The idea is similar.
# Let's assume 2 means in this stage it is dead, but in the next stage, it will alive.
# Assme 3 means in this stage it is alive, but in the next stage it will dead.
# When will calculating count, we can use '%2'.
# Time complexity: O(N^2)

# 3. Infinite dimensions.
# https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution


class Solution1:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        res = []
        for i in range(n):
            res.append([])
            for j in range(m):
                temp = self.helper(board, i, j, n, m)
                if board[i][j] == 1:
                    if temp < 2:
                        res[i].append(0)
                    elif temp == 2 or temp == 3:
                        res[i].append(1)
                    else:
                        res[i].append(0)
                else:
                    if temp == 3:
                        res[i].append(1)
                    else:
                        res[i].append(0)
        board[:] = res
        
        
    def helper(self, board, i, j, n, m):
        count = 0
        if i > 0 and j > 0:     count += board[i-1][j-1]
        if i > 0:               count += board[i-1][j]
        if i > 0 and j < m-1:   count += board[i-1][j+1]
        if j > 0:               count += board[i][j-1]
        if j < m-1:             count += board[i][j+1]
        if i < n-1 and j > 0:   count += board[i+1][j-1]
        if i < n-1:             count += board[i+1][j]
        if i < n-1 and j < m-1: count += board[i+1][j+1]
        return count

class Solution2(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                temp = self.helper(board, i, j, n, m)
                if board[i][j] == 0 or board[i][j] == 2:
                    if temp == 3:
                        board[i][j] = 2
                else:
                    if temp < 2 or temp > 3:
                        board[i][j] = 3
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0
        
        
    def helper(self, board, i, j, n, m):
        count = 0
        if i > 0 and j > 0:     count += board[i-1][j-1]%2
        if i > 0:               count += board[i-1][j]%2
        if i > 0 and j < m-1:   count += board[i-1][j+1]%2
        if j > 0:               count += board[i][j-1]%2
        if j < m-1:             count += board[i][j+1]%2
        if i < n-1 and j > 0:   count += board[i+1][j-1]%2
        if i < n-1:             count += board[i+1][j]%2
        if i < n-1 and j < m-1: count += board[i+1][j+1]%2
        return count


class Solution3(object):
    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
        return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}