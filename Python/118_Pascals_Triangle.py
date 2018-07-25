"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows > 2:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                tem_list = result[-1]
                new_list = [1]
                for j in range(i-1):
                    new_list.append(tem_list[j] + tem_list[j+1])
                new_list.append(1)
                result.append(new_list)
            return result
        else:
            if numRows == 2:
                return [[1], [1, 1]]
            elif numRows == 1:
                return [[1]]
            else:
                return []
