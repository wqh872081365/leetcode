"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2:
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        d = []
        for i in range(len(matrix)):
            d.append([])
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    d[i].append(0)
                else:
                    if i > 0:
                        if j > 0:
                            d[i].append(min(d[i-1][j]+1, d[i][j-1]+1))
                        else:
                            d[i].append(d[i-1][j]+1)
                    else:
                        if j > 0:
                            d[i].append(d[i][j-1]+1)
                        else:
                            d[i].append(len(matrix)+len(matrix[i]))
        for i in range(len(matrix))[::-1]:
            for j in range(len(matrix[i]))[::-1]:
                if i<len(matrix)-1:
                    if j < len(matrix[i])-1:
                        d[i][j] = min(d[i+1][j]+1, d[i][j+1]+1, d[i][j])
                    else:
                        d[i][j] = min(d[i+1][j]+1, d[i][j])
                else:
                    if j < len(matrix[i])-1:
                        d[i][j] = min(d[i][j+1]+1, d[i][j])
                    else:
                        pass
        return d