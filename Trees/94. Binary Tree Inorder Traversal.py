# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        x = []
        if root:
            x.extend(self.inorderTraversal(root.left))
            x.append(root.val)
            x.extend(self.inorderTraversal(root.right))
        return x
    def inorderTraversal2(self, root):
        res = []
        if root == None:
            return None
        stack = [root]
        curr = root.left
        while curr or stack:
            if not curr:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
            
            
        return res
    
    def inorderTraversal(self, root):
        res = []
        if root == None:
            return None
        stack = []
        top = root
        
        while top or stack:
            while top:
                stack.append(top)
                top = top.left
            top = stack.pop()
            res.append(top.val)
            top = top.right
            
        return res            
            
            
        
