#neet
class Node:
    def __init__(self):
        self.childrens = {}
        self.isword = False

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        if not word:
            return
        cur = self.root
        
        for i in word:
            if i not in cur.childrens:
                cur.childrens[i] = Node()
            cur = cur.childrens[i]
        
        cur.isword = True

    def search(self, word: str) -> bool:
        if not word:
            return
        cur = self.root
        for i in word:
            if i not in cur.childrens:
                return False
            cur = cur.childrens[i]
        
        return cur.isword

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return
        cur = self.root
        for i in prefix:
            if i not in cur.childrens:
                return False
            cur = cur.childrens[i]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
