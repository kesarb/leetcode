"""
783. Minimum Distance Between BST Nodes

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = -1
        self.res = float("inf")
        def rec(r):
            if not r:
                return
            
            rec(r.left)
            if self.prev != -1:
                self.res = min(r.val-self.prev, self.res)
            self.prev = r.val
            rec(r.right)
        
        rec(root)
        return self.res
      
