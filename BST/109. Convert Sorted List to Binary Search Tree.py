"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 
"""

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    
    def sortedListToBST(self, head):
        self.head = head
        def rec(start, end):
            if self.head == None:
                return None
            
            if start > end:
                return None
            
            if start == end:
                val = self.head.val
                self.head = self.head.next
                return TreeNode(val)

            mid = start + (end-start)//2
            
            left = rec(start, mid-1)# build left tree
            
            root = TreeNode(self.head.val) # middle node
            self.head = self.head.next
            root.left = left
            
            root.right = rec(mid+1, end) # build right tree
            
            
            
            
            return root
            
        cur = head
        ctr = 0
        while cur :
            ctr += 1
            cur = cur.next

        return rec(0, ctr-1)
