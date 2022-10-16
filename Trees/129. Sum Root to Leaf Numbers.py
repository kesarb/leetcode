"""
129. Sum Root to Leaf Numbers

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.sum = 0
        def rec(r, v):
            if not r:
                return
            if not r.left and not r.right:
                self.sum += v*10+r.val
                return
            rec(r.left, v*10+r.val)
            rec(r.right, v*10+r.val)
        
        rec(root, 0)
        return self.sum
