class Solution:
    def numTrees(self, n: int) -> int:
        res = [1]*(n+3)
        res[2] = 2
        res[3] = 5
        for i in range(4, n+1):
            res[i]  = 0
            for j in range(1, i+1):
                left= j-1
                right = i-j
                res[i] += res[left]*res[right]
        return res[n]
                
        
