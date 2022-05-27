"""

Hard

4752

213

Add to List

Share
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = ""
        
        for i in p:
            if not r or (i is not '*' or r[-1] is not '*' ):
                r += i
        p = r
        
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)] 
        
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
        
        return dp[m][n]
    
    def isMatch1(self, s: str, p: str) -> bool:
        
        @cache
        def rec(i,j):
            if j>=len(p) and i>= len(s):
                print(i,j)
                return True
            if j>=len(p):
                return False
            if i>=len(s):
                if p[j:] == '*'*(len(p)-j):
                    return True
                return False
            if p[j] == '*':
                return rec(i, j+1) or rec(i+1, j)
            if s[i] == p[j] or p[j] == '?':
                return rec(i+1, j+1)
            return False
        
        return rec(0,0)
    
    
    
