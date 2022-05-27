"""
234. Palindrome Linked List
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head1: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if head1 == None or head1.next == None:
            return head1, None
        
        dummy = ListNode()
        dummy.next = head1
        
        head2 = None
        
        slow = dummy
        fast = dummy
        while fast and fast.next:
            fast = fast.next and fast.next.next
            slow = slow.next
            
        head2=slow.next
        slow.next = None
        return head1, head2
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1, l2 = self.partition(head)
        l2  = self.reverseList(l2)
        while l1 and l2 and l1.val == l2.val:
            l1 = l1.next
            l2 = l2.next
            
        if l1 and l2:
            return False
        return True
