"""
285. Inorder Successor in BST

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root1: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        root = root1
        parent = None
        while root:
            if root.val == p.val:
                break
            
            if root.val > p.val:
                
                parent = root
                root = root.left
            else:
                root = root.right
                
        if not root.right:
            return parent
        r= root.right
        while r.left:
            r= r.left
        
        return r
        
