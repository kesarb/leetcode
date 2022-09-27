"""
498. Diagonal Traverse
Medium

2558

575

Add to List

Share
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
Accepted
224,150
Submissions
387,279
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        
        row = 0
        col = 0
        up = True
        
        for i in range(m*n):
            if row == m or col == n or row == -1 or col == -1:
                if up:
                    if col == n:
                        row = row + 1
                        col = col - 1
                    row = row + 1
                else:
                    if row == m:
                        row = row - 1
                        col = col + 1
                    col = col + 1
                up = not up
            if up:
                while row >= 0 and col<n:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                while col >= 0 and row<m:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                
        return res
            
        
