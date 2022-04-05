"""
695. Max Area of Island
Medium

5701

144

Add to List

Share
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def isSafe(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            return False
        
        def rec(i,j, grid):
            grid[i][j] = 0
            self.local_length += 1
            for i1, j1 in [(-1,0), (1,0), (0, 1), (0,-1)]:
                i1 = i1 + i
                j1 = j1 + j
                
                if isSafe(i1,j1) and grid[i1][j1] == 1:
                    
                    rec(i1,j1, grid)
        res = 0 
        self.local_length = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.local_length = 0
                    rec(i,j, grid)
                    res = max(self.local_length, res)
        return res
                    
                
