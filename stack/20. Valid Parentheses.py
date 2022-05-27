"""
20. Valid Parentheses
Easy

13205

589

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
2,267,498
Submissions
5,549,441


"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {"(": ")", "{":"}", "[": "]"}
        for i in s:
            if i in matches:
                stack.append(i)
            else:
                top =  stack.pop() if len(stack) != 0 else ""
                if top not in matches or matches[top] != i:
                    return False
        if len(stack) == 0:
            return True
        return False
        
