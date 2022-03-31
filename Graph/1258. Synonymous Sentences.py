"""
1258. Synonymous Sentences
Medium

You are given a list of equivalent string pairs synonyms where synonyms[i] = [si, ti] indicates that si and ti are equivalent strings. You are also given a sentence text.

Return all possible synonymous sentences sorted lexicographically.

 

Example 1:

Input: synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"
Output: ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]

 

Constraints:

    0 <= synonyms.length <= 10
    synonyms[i].length == 2
    1 <= si.length, ti.length <= 10
    si != ti
    text consists of at most 10 words.
    The words of text are separated by single spaces.


"""

from collections import defaultdict

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        ctr = 0
        s = defaultdict(set)
        d = defaultdict(list)
        for i,j in synonyms:
            d[i].append(j)
            d[j].append(i)
 
        visit = {}
        def dfs(i, ctr, d, visit):
            if i in visit:
                return
            
            s[ctr].add(i)
            visit[i] = ctr
            for j in d[i]:
                dfs(j, ctr, d, visit)
            
                
        ctr = 0
        for i in d:
            if i not in visit:
                dfs(i, ctr, d, visit)
                ctr += 1
                
        
        words = text.split(" ")
        d = visit
        self.res = []
        def rec(current, res):
            if not current:
                self.res.append(res.strip())
                return
                
            if current[0] not in d:
                rec(current[1:], res+" "+current[0])
                return
            
            l = list(s[d[current[0]]])
            l.sort()
            
            for each in l:
                rec(current[1:], res+" "+each)
        
        rec(words, "")
        return self.res
                
            
        
