"""
1958. Check if Move is Legal

You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:
"""

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        
        neighbours = [(1,0), (0,1), (-1, 0), (0, -1), \
                     (-1, 1), (-1, -1), (1, -1), (1,1)]
        
        m = len(board)
        n = len(board[0])
        
        def canMove(x, y):
            x1 = rMove+x
            y1 = cMove+y
            length = 1
            while 0<=x1<m and 0<=y1<n and board[x1][y1] != '.':
                if board[x1][y1] != color:
                    length+=1
                else:
                    return length >= 2
                x1 = x1+x
                y1 = y1+y
                
            return False
        
        for x, y in neighbours:
            if canMove(x, y):
                return True
        
        return False
