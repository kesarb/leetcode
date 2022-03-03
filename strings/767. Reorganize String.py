"""
767. Reorganize String
Medium

4313

170

Add to List

Share
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = [0]*26
        output = []
        for each in s:
            dic[ord(each)-ord('a')] += 1
        
        char = []
        for e, val in enumerate(dic):
            if val >= 1:
                char.append([-1*val, chr(e+ord('a'))])
                
        heapq.heapify(char)
        #print(char)
        i = 0
        output= []
        os = ""
        while len(char) > 1:
            #print(char)
            val1, c1 = heapq.heappop(char)
            val2, c2 = heapq.heappop(char)
            val1 += 1
            val2 +=1
            if os and os[-1] != c1:
                os += ""+c1 + c2
            else:
                os += ""+c1 + c2
            
            if val1 != 0:
                heapq.heappush(char, [val1,c1])
            if val2 != 0:
                heapq.heappush(char, [val2,c2])
        if len(char) == 0:
            return os
        if len(char) == 1 and char[0][0] == -1 and os[-1] != char[0][1]:
            return os+char[0][1]
        if len(char) == 1 and char[0][0] == -1 and os[0] != char[0][1]:
            return char[0][1]+os
        return ""
            
            
