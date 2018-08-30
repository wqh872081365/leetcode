"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 2
                    if i > 0:
                        if grid[i-1][j] < grid[i][j]:
                            res += grid[i][j] - grid[i-1][j]
                    else:
                        res += grid[i][j]
                    if j > 0:
                        if grid[i][j-1] < grid[i][j]:
                            res += grid[i][j] - grid[i][j-1]
                    else:
                        res += grid[i][j]
                    if i < m - 1:
                        if grid[i+1][j] < grid[i][j]:
                            res += grid[i][j] - grid[i+1][j]
                    else:
                        res += grid[i][j]
                    if j < n - 1:
                        if grid[i][j+1] < grid[i][j]:
                            res += grid[i][j] - grid[i][j+1]
                    else:
                        res += grid[i][j]
        return res
