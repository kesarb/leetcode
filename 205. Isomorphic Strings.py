"""
205. Isomorphic Strings
Easy

3323

628

Add to List

Share
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic1 = {}
        bitarray = [False]*128
        
        for i in range(len(s)):
            s1 = s[i]
            t1 = t[i]
            if s1 not in dic1:
                asciicode = ord(t1)-ord('a') 
                if bitarray[asciicode]:
                    return False
                bitarray[asciicode] = True
                dic1[s1] = t1
            else:
                if dic1[s1] != t1:
                    return False
        return True
    
    def isIsomorphic(self, s, t):
        
        def dummy(s):
            d = {}
            res = []
            
            for index, ch in enumerate(s):
                if ch not in d:
                    d[ch] = index
                res.append(str(d[ch]))
            return " ".join(res)
        
        return dummy(s) == dummy(t)
    
    
                
            
        
        
        
