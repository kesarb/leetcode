"""
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        neighbours = [(-1,0), (1,0), (0,-1), (0, 1)]    
        visit = [[0 for i in range(n)] for j in range(m)]
        @cache
        def isSafe(i, j):
            if 0<=i<m and 0<=j<n:
                return True
            return False
        
        def dfs(i,j, visit, word):
            if len(word) == 0:
                return True
            if visit[i][j]:
                return False
            
            visit[i][j] = 1
            
            for i1, j1 in neighbours:
                if isSafe(i+i1,j+j1) and not visit[i+i1][j+j1] and  word[0]== board[i+i1][j+j1]:
                    if dfs(i+i1, j+j1, visit, word[1:]):
                        return True
            visit[i][j] = 0
            return False

            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j, visit, word[1:]):
                    return True
                
        return False
    
            
