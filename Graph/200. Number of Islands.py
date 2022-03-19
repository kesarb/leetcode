"""
200. Number of Islands
Medium

12874

317

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def issafe(g,i,j):
            if 0<=i <m and 0<=j<n:
                return g[i][j] == "1"
            return False
        
        def dfs(grid, i, j):
            
            grid[i][j] = "0"
            
            neigbhours = [(-1,0), (1,0), (0, 1), (0,-1)]
            
            for e1,e2 in neigbhours:
                if issafe(grid, i+e1, j+e2):
                    dfs(grid, i+e1, j+e2)
                
        ctr = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ctr += 1
                    dfs(grid, i,j)
        return ctr
