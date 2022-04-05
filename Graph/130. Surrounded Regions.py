"""
130. Surrounded Regions
Medium

4642

1150

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def rec(i,j, board):
            board[i][j] = 'P'
            for i1, j1 in [(0,1), (0, -1), (1,0), (-1,0)]:
                i1 = i+i1
                j1 = j+j1
                if (0<=i1<m and 0<=j1<n) and board[i1][j1] == 'O':
                    rec(i1, j1, board)
        
        for i in range(m):
            if board[i][0] == 'O':
                rec(i,0, board)
            if board[i][n-1] == 'O':
                rec(i, n-1,board)
        
        for i in range(n):
            if board[0][i] == 'O':
                rec(0,i, board)
            if board[m-1][i] == 'O':
                rec(m-1, i, board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'                    
                
                
                
                
