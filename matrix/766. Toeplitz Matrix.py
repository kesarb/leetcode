"""
766. Toeplitz Matrix
Easy

1875

117

Add to List

Share
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] 
"""


class Solution:
    def isToeplitzMatrix(self, M: List[List[int]]) -> bool:
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                
                if i>0 and j > 0 and M[i-1][j-1] != M[i][j]:
                    return False
        return True
        
    def isToeplitzMatrix_daigonal(self, M: List[List[int]]) -> bool:
        m = len(M)
        n = len(M[0])
        ctr = 0
        row = 0
        col = n
        dx = 0
        dy = -1
        
        while ctr <(m+n)-1:
            row += dx
            col += dy
            
            i = row
            j = col 
            #print(ctr, i,j)
            val = M[i][j]
            while i<m and j<n:
                if M[i][j] != val:
                    return False
                i += 1
                j += 1
            if col == 0:
                dx, dy = 1, 0
            ctr+=1
            
        return True
            
        
