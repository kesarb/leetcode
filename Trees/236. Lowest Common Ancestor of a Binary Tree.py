class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        a = self.lowestCommonAncestor(root.left, p , q)
        b = self.lowestCommonAncestor(root.right, p ,q)

        if root == p or root == q:
            if a == None:
                b = root
            else:
                a = root

        if a and b:
            return root

        return a or b
