"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = {}
        count = 0
        m = len(grid)
        n = len(grid[0])

        def find_one(i, j):
            res.setdefault(i, {})[j] = True
            c = 1
            if i - 1 >= 0 and grid[i - 1][j] and not res.get(i - 1, {}).get(j):
                c += find_one(i - 1, j)
            if i + 1 <= m - 1 and grid[i + 1][j] and not res.get(i + 1, {}).get(j):
                c += find_one(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] and not res.get(i, {}).get(j - 1):
                c += find_one(i, j - 1)
            if j + 1 <= n - 1 and grid[i][j + 1] and not res.get(i, {}).get(j + 1):
                c += find_one(i, j + 1)
            return c

        for i, g in enumerate(grid):
            for j, v in enumerate(g):
                if not res.get(i, {}).get(j):
                    if v == 1:
                        count = max(count, find_one(i, j))
        return count
