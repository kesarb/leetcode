"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        def rec(t, a, b):
            if not t:
                return None

            self.max = max(self.max, abs(t.val - a), abs(t.val-b))

            min1 = min(a,b,t.val)
            max1 = max(a,b,t.val)

            rec(t.left, min1, max1)
            rec(t.right, min1, max1)
            
            
            
        rec(root, root.val, root.val)
        return self.max
