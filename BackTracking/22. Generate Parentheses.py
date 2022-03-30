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
        
                
                
        
