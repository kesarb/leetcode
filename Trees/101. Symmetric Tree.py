"""
101. Symmetric Tree

101. Symmetric Tree
Easy

11091

253

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _aux(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return _aux(t1.left, t2.right) and _aux(t1.right,t2.left)
        return _aux(root.left, root.right)
        
