"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        
        m = len(M)
        n = len(M[0])
        res = 0
        for i in range(m):
            M[i][0] = int(M[i][0])
            res = max(res, M[i][0])
        
        for i in range(n):
            M[0][i] = int(M[0][i])
            res = max(res, M[0][i])
        print(M)
        for i in range(1,m):
            for j in range(1, n):
                if M[i][j] == '1':
                    M[i][j] = min(M[i-1][j-1], M[i-1][j], M[i][j-1]) + 1
                    res = max(M[i][j], res)
                else:
                    M[i][j] = 0
                    
        return res*res
                
            
        
