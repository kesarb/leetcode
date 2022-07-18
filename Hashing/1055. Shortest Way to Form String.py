"""
1055. Shortest Way to Form String
Medium

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

 

Constraints:

    1 <= source.length, target.length <= 1000
    source and target consist of lowercase English letters.


"""

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
		# First, iterate through the source to find the characters that follows the current one. 
		# If there are more than for a certain following character, consider the first one.
		# Running time O(len(source)); space O(len(source) X 26) = O(len(source))
        dic = {}
        for i in range(len(source))[::-1]:
            c = source[i]
            dic[i] = {} if i + 1 not in dic else dic[i + 1].copy()
            dic[i][c] = i + 1
        # For source = 'abba' the table looks like this: 
		# {3: {'a': 4}, 2: {'a': 4, 'b': 3}, 1: {'a': 4, 'b': 2}, 0: {'a': 1, 'b': 2}}
		
        result = 0
        ind = 0
		# Then, iterate throught the target characters
		# Running time O(len(target))
        for char in target:
			# dic[0] contains all characters in the source
            if char not in dic[0]: return -1
			
			# If 'ind' points to the last character of the source or the current character does not exist in the 
			# possible set of characters indicated by 'ind', this means a new subsequence has started
            if ind == len(source) or char not in dic[ind]:
                ind = 0
                result += 1
			
			# Update the index
            ind = dic[ind][char]
		
		# After the last increment (two lines above), at least one valid character has been observed
        return result + 1
