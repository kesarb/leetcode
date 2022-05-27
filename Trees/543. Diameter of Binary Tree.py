"""
543. Diameter of Binary Tree
Easy

7942

495

Add to List

Share
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        
        def rec(root):
            if not root:
                return 0
            l = rec(root.left)
            r = rec(root.right)
            self.max = max(self.max, l+r)
            return 1+max(l,r)
        rec(root)
        return self.max
