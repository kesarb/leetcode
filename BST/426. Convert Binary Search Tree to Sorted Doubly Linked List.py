"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        first = last = None
        def rec(r):
            if not r:
                return
            rec(r.left)
            nonlocal last, first
            if first == None:
                first = r
            if last:
                last.right = r
                r.left = last
            last = r
            
            rec(r.right)
        
        rec(root)
        first.left = last
        last.right = first
        
        return first
            
