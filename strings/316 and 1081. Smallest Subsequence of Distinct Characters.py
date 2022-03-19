"""
316. Remove Duplicate Letters
or
1081. Smallest Subsequence of Distinct Characters
Medium

1562

140

Add to List

Share
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""

from collections import defaultdict
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        d = defaultdict(int)
        for i, c in enumerate(s):
            d[c]+=1
        
        stack = []
        
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and d[stack[-1]]:
                    stack.pop()
                stack.append(c)
            d[c]-=1
        
        return "".join(stack)
