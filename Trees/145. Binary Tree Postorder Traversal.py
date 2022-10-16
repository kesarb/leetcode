"""
145. Binary Tree Postorder Traversal

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        curr = root
        stack = []
        prev = None
        res = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack[-1].right and prev != stack[-1].right:
                curr = stack[-1].right
            else:
                t = stack.pop()
                res.append(t.val)
                prev=t
        return res
        
