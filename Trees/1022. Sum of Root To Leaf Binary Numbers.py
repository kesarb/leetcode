"""
1022. Sum of Root To Leaf Binary Numbers
Easy

2424

146

Add to List

Share
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
"""

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def rec(root, s):
            if root == None:
                return
            
            s =  s <<1 | root.val
            
            if root.left == None and root.right == None:
                self.res += s
                return
            
            rec(root.left, s)
            rec(root.right, s)
            
        rec(root, 0)
        return self.res
