"""
3. Longest Substring Without Repeating Characters
"""

class Solution:
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        max_length = 0
        set1 = set() 
        start = 0
        for i, val in enumerate(s):
            if val in set1:
                while(start < i and s[start] != val):
                    set1.remove(s[start])
                    start += 1
                set1.remove(val)
                start += 1
            set1.add(val)
            max_length = max(len(set1),max_length)
                
        return max(len(set1),max_length)
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        d = dict()
        
        start = 0
        for i, val in enumerate(s):
            if val in d:
                start = max(start, d[val]+1)
            max_length = max(max_length, i-start+1)    
            d[val] = i
        return max_length
