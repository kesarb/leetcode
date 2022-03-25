"""
212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.


"""
class Node():
    def __init__(self):
        self.childrens = {}
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        if not word:
            return
        curr = self.root

        for each in word:
            if each not in curr.childrens:
                curr.childrens[each] = Node()
            curr = curr.childrens[each]
        curr.isWord = True
        curr.word = word
        

    def print(self):
        curr = self.root

        def rec(curr, s):
            if not curr:
                print("Somthing is missing")
            if curr.isWord:
                print(s)
            for each in curr.childrens:
                rec(curr.childrens[each], s + each)

        rec(curr, "")


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct Trie
        #   TreeBuild(O(n*maxlen(word))
        #   Expose the print and get Node all childrens

        # take each cell and find whether will get word or not using dfs prcodudre
        # let say cell contains 'o', get the all the node starts with 'o' position (i,j)
        # even if its word expolore till completing the dfs untill no words found
        m = len(board)
        n = len(board[0])

        trie = Trie()
        for each in words:
            trie.addWord(each)

        root = trie.root
        res = set()

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @cache
        def isSafe(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        def dfs(i, j, node):
            if not node or board[i][j]=='#':
                return ""

            if node.isWord == True:
                res.add(node.word)
            letter = board[i][j]
            board[i][j] = '#'

            for u, v in neighbours:
                u1 = i + u
                v1 = j + v

                if isSafe(u1, v1) and board[u1][v1]!='#':
                    c = board[u1][v1]
                    if c in node.childrens:
                        dfs(u1, v1, node.childrens[c])
                        
            board[i][j]=letter

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.childrens:
                    dfs(i, j, root.childrens[board[i][j]])

        return list(res)

