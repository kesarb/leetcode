"""
139. Word Break
Medium

9923

441

Add to List

Share
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

class Solution:
    #time complexity O(n*m*comp)
    
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[n]=True
        word_list = [(w, len(w) )for w in wordDict]
        
        for i in range((n)-1, -1, -1):
            last_word = s[i:]
            for w, l in word_list:
                if last_word.startswith(w):
                    dp[i] = dp[i+l]
                if dp[i] == True:
                    break
                    
        return dp[0]
                
        
        
    
    
    
    #time complexity O(n*n*comparison)
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n]=True
        for i in range((n)-1, -1, -1):
            for j in range(i, n):
                if dp[j+1] == True:
                    if s[i:j+1] in wordDict:
                        dp[i] = True
                        break
        
        return dp[0]
    
    #time complexity O(n*n*comp))
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def rec(word):
            if word in cache:
                return cache[word]
            if not word or word in wordDict:
                cache[word]=True
                return True
            
            s = ""
            for index, each in enumerate(word):
                s+=each
                if s in wordDict:
                    if rec(word[index+1:]):
                        cache[word]=True
                        return True
            cache[word]=False
            return False
        
        return rec(s)
   
