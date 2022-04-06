"""
329. Longest Increasing Path in a Matrix
Hard

5092

87

Add to List

Share
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        def dfs(i,j, dp, visit):
            if (i,j) in visit:
                return dp[i][j]
            visit.add((i,j))
            for i1, j1 in [(1,0),(0,1), (0,-1),(-1,0)]:
                u = i1+i
                v = j1+j
                if 0<=u<m and 0<=v<n and matrix[u][v] > matrix[i][j]:
                    dp[i][j] = max(dfs(u,v, dp,visit)+1, dp[i][j])
                    
            return dp[i][j]
        res = 1    
        visit = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in visit:
                    dp[i][j] = dfs(i,j, dp, visit)
                    res = max(res, dp[i][j])
                    
        return res
            
