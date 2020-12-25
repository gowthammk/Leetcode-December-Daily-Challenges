# Diagonal Traverse
#
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
# diagonal order as shown in the below image.
#
#
#
# Example:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.

class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, 0
        result = []
        for i in range(rows * cols):
            result.append(matrix[row][col])
            if (row + col) % 2 == 0:
                if col == (cols - 1):
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == (rows - 1):
                    col += 1
                elif col == 0:
                    row += 1

                else:
                    row += 1
                    col -= 1
        return result