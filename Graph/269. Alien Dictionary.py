"""
269. Alien Dictionary
Hard

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.

"""

from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set()
        g = defaultdict(list)
        indegree={}
        prev = words[0]
        letters = letters.union(set(prev))
        for w in words:
            n1 = len(w)
            n2 = len(prev)
            
            i = 0
            while i < (n1):
                if i >= n2 or prev[i] != w[i]:
                    break
                i+=1
            
            letters = letters.union(set(w))
            
            if i != n1 and i != n2:
                indegree[w[i]] = indegree.get(w[i], 0)+1
                g[prev[i]].append(w[i])
            if i == n1 and i < n2:
                return ""
            prev = w
        
        queue = []
        for each in letters:
            if each not in indegree:
                queue.append(each)
        res = ""
        while queue:
            w = queue.pop(0)
            res = res+w
            if w in g:
                for each in g[w]:
                    indegree[each] -= 1
                    if indegree[each] == 0:
                        queue.append(each)
                        
        return res if len(res) == len(letters) else ""
