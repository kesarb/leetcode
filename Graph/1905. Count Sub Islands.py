"""
1905. Count Sub Islands
Medium
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""
class Solution:
    def countSubIslands(self, g: List[List[int]], f: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        
        res = 0
        
        def dfs(i,j):
            flag = True
            for i1, j1 in [(1,0),(0,1), (0,-1),(-1,0)]:
                u = i+i1
                v = j+j1
                if 0<=u<m and 0<=v<n and f[u][v] == 1:
                    f[u][v] = 0
                    if g[u][v] == 0:
                        flag = False
                    flag = dfs(u,v) and flag
                    
            return flag
        
        for i in range(m):
            for j in range(n):
                if f[i][j] == 1 and g[i][j] == 1: 
                    f[i][j] = 0
                    if dfs(i,j):
                        res += 1
        return res
    
                    
        
        
