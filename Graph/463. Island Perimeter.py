"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def issafe(i,j):
            if 0<=i <m and 0<=j<n:
                return grid[i][j] == 1
            return False
        
        visit = set()
        
        def dfs(grid, i, j):
            
            visit.add((i,j))
            
            neigbhours = [(-1,0), (1,0), (0, 1), (0,-1)]
            s1=0
            for e1,e2 in neigbhours:
                if issafe(i+e1, j+e2):
                    if (i+e1,j+e2) not in visit:
                        s1 += dfs(grid, i+e1, j+e2)
                else:
                    s1+=1
                    
            return s1
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(grid, i,j)
        return 0
