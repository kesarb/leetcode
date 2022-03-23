"""
417. Pacific Atlantic Water Flow
Medium

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        blue = [[i for i in range(n)] for j in range(m)]
        red  = [[i for i in range(n)] for j in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                red[i][j] = 0
                blue[i][j] = 0
                
        def isSafe(i, j):
            if 0<=i<m and 0<=j<n:
                return True
            return False
        
        neighbours = [(-1,0), (1,0), (0,-1), (0, 1)]    
        
        def dfs(i, j, visit):
            if visit[i][j] == 1:
                return
            visit[i][j] = 1
            for i1, j1 in neighbours:
                if isSafe(i+i1,j+j1) and not visit[i+i1][j+j1] and heights[i][j] <= heights[i+i1][j+j1]:
                    dfs(i+i1, j+j1, visit)
        
        
        for i in range(0,m):
            dfs(i, n-1, blue)
            dfs(i, 0, red)
                
        for j in  range(0,n):
            dfs(m-1, j, blue)
            dfs(0, j, red)
                
        res = []
        for i in range(m):
            print(red[i])
            for j in range(n):
                if red[i][j] == 1 and blue[i][j] == 1:
                    res.append([i,j])
        return res
    
