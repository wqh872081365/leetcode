"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix:
            result = []
            for j in range(len(matrix)):
                result.append(([1] if matrix[j][0] == "1" else [0]))
            for i in range(1, len(matrix[0])):
                result[0].append((1 if matrix[0][i] == "1" else 0))
            for j in range(1, len(matrix)):
                for i in range(1, len(matrix[0])):
                    result[j].append((min(result[j][i-1], result[j-1][i-1], result[j-1][i])+1 if matrix[j][i] == "1" else 0))
            return max([max(i) for i in result])**2
        else:
            return 0