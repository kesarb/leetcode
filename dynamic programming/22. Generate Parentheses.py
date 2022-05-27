"""
22. Generate Parentheses
Medium

13002

498

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def rec(op, cl, st):
            if op == cl == 0:
                res.append(st)
                return
            
            if op>0:
                rec(op-1, cl, st+'(')
            if cl>0 and op<cl:
                rec(op, cl-1, st+')')
        
        rec(n, n, "")
        return res
        
                
                
        
