"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.
"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.s = [[]]
        if len(matrix) and len(matrix[0]):
            self.s[0].append(matrix[0][0])
            for i in range(1, len(matrix)):
                self.s.append([matrix[i][0] + self.s[i - 1][0]])
            for j in range(1, len(matrix[0])):
                self.s[0].append(matrix[0][j] + self.s[0][j - 1])
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    self.s[i].append(self.s[i - 1][j] + self.s[i][j - 1] - self.s[i - 1][j - 1] + matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1:
            if col1:
                return self.s[row2][col2] + self.s[row1 - 1][col1 - 1] - self.s[row2][col1 - 1] - self.s[row1 - 1][col2]
            else:
                return self.s[row2][col2] - self.s[row1 - 1][col2]
        else:
            if col1:
                return self.s[row2][col2] - self.s[row2][col1 - 1]
            else:
                return self.s[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)