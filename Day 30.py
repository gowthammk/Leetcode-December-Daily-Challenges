# Game of Life
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular
# automaton devised by the British mathematician John Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0). Each cell interacts with its
# eight neighbors (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell
# in the current state, where births and deaths occur simultaneously. Given the current
# state of the m x n grid board, return the next state.
#
#
#
# Example 1:
#
#
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:
#
#
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
#

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = set((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y)
        for i in range(0, m):
            for j in range(0, n):
                live = 0
                for x, y in directions:
                    if (i + x < m and i + x >= 0) and (j + y < n and j + y >= 0) and abs(board[i + x][j + y]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                if live == 3 and board[i][j] == 0:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board
