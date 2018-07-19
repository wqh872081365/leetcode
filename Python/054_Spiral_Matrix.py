"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            matrix_len = len(matrix)
            if matrix_len == 1:
                result += matrix[0]
                break
            elif matrix_len == 2:
                result += matrix[0]
                result += matrix[1][::-1]
                break
            else:
                sub_matrix_len = len(matrix[0])
                if sub_matrix_len == 1:
                    result += [sub_matrix[0] for sub_matrix in matrix]
                    break
                elif sub_matrix_len == 2:
                    result += matrix.pop(0)
                    result += [sub_matrix[1] for sub_matrix in matrix]
                    result += [sub_matrix[0] for sub_matrix in matrix][::-1]
                    break
                else:
                    result += matrix.pop(0)
                    for sub_matrix in matrix[0:-1]:
                        result.append(sub_matrix.pop())
                    result += matrix.pop()[::-1]
                    for sub_matrix in matrix[::-1]:
                        result.append(sub_matrix.pop(0))
        return result
