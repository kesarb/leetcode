"""
211. Design Add and Search Words Data Structure
Medium

4668

195

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class Trie:
    def __init__(self):
        self.children = {}
        self.isword = False
        
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        
        for i in word:
            if i not in cur.children:
                cur.children[i] = Trie()
            cur = cur.children[i]
        cur.isword = True
        
    def print1(self):
        dic = []

        def rec(p,s):
            if not p:
                return
            if p.isword == True:
                dic.append(s)
                
            for i in p.children:
                rec(p.children[i], s+i)
                
        rec(self.root, "")
        print(dic)
        
    def search(self, word: str) -> bool:
        #self.print1()
        def rec(p, w):
            if not w and p.isword:
                return True
            
            if not p or not w:
                return False
            if w[0] == '.':
                for i in p.children:
                    #print(i,"eewew")
                    if rec(p.children[i], w[1:]):
                        return True
                return False
            else:
                if w[0] not in p.children:
                    return False
                return rec(p.children[w[0]], w[1:])
                
                
        return rec(self.root, word)
            
