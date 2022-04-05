"""
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []
        d = {}
        def rec(m):
            if m in d:
                return d[m]
            if m == 1:
                d[m] = [TreeNode(0)]
                return d[m]
            #print(m)
            res = []
            for i in range(2, m+1):
                if (i-1) % 2 != 0:
                    leftNodes = rec(i-1)
                    rightNodes = rec(m-i)
                    for each in leftNodes:
                        for each1 in rightNodes:
                            node = TreeNode(0)
                            node.left=each
                            node.right = each1
                            res.append(node)
            d[m] = res
            return res
        output = rec(n)
        #print(d)
        return output
