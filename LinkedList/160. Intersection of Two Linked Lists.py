# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        s = set()
        curr = headA
        m = 0
        n = 0
        while curr:
            m +=1
            curr = curr.next
        curr = headB
        while curr:
            n += 1
            curr = curr.next
        
        k = abs(m-n)
        if n > m:
            headA, headB, m, n = headB, headA, n, m
        curr1 = headA
        #print(k)
        while k > 0:
            curr1 = curr1.next
            k -= 1
        
        curr2 = headB
        #print(k, curr1, curr2 )
        while curr1 and curr2 and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1 and curr1 == curr2:
            return curr1
        
        return None
    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        s = set()
        curr = headA
        while curr:
            s.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in s:
                return curr
            curr = curr.next
        return None
