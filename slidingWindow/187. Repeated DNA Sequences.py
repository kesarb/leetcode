"""
187. Repeated DNA Sequences
187. Repeated DNA Sequences
Medium

1925

404

Add to List

Share
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = set()
        input_str = s[:10]
        d.add(input_str)
        i = 1
        res = set()
        for j in range(10, len(s)):
            input_str = s[i:j+1]
            if input_str in d and input_str not in res:
                res.add(input_str)
            
            if input_str not in d:
                d.add(input_str)
                
            i+=1
        return list(res)

