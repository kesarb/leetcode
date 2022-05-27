"""
10. Regular Expression Matching


Share
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)] 
        
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2] 
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j - 2];
                    if p[j-2] == '.' or p[j-2] == s[i-1] :
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and( p[j-1] == '.' or p[j-1] == s[i-1] )
        
        return dp[m][n]
    
    def isMatchrec(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        @cache
        def dfs(l, r):
            if l>=m and r>=n:
                return True
            if r>=n:
                return False
            
            match = l<m and (s[l] == p[r] or p[r] == '.')
            
            if r+1 <n  and p[r+1] == '*':
                return  dfs(l, r+2) or (match and dfs(l+1, r))
            
            if match:
                return dfs(l+1, r+1)
            return False
            
        return dfs(0,0)
    
