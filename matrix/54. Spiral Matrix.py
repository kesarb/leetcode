"""
54. Spiral Matrix.py
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        res = []
        while top <bottom and left<=right:
                
            for i in range(left, right+1):
                res.append(matrix[top][i])
                
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
                
            if left != right:
                for i in range(right-1, left, -1):
                    res.append(matrix[bottom][i])

                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
                
            top +=1
            bottom-=1
            left +=1
            right -=1
            
        if top == bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i]) 
        
            
        return res
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        res = []
        row = 0
        col = 0
        visits = n
        dx = 0
        dy = 1
        direction = 0
        i = 0
        while i < m*n:
            res.append(matrix[row][col])
            visits-=1
            if visits == 0:
                visits = m*((direction+1)%2)+n*((direction)%2)-(direction//2)-1
                dx,  dy = dy, -1*dx
                direction +=1
            row +=dx
            col +=dy
            i+=1
        return res
            
        
