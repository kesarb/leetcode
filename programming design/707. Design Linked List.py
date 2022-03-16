"""
707. Design Linked List
Medium

1367

1138

Add to List

Share
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        node = self.findNode(index)
        if node:
            return node.val
        return -1
    
    def add(self, current_node, val):
        new_node = Node(val)
        new_node.prev = current_node
        new_node.next = current_node.next
        
        current_node.next.prev = new_node
        current_node.next = new_node
        
    def addAtHead(self, val: int) -> None:
        self.add(self.head, val)
        
    def addAtTail(self, val: int) -> None:
        self.add(self.tail.prev, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.findNode(index, True)
        if node:
            node = node.prev
            if node:
                self.add(node,val)

    def deleteAtIndex(self, index: int) -> None:
        node = self.findNode(index)
        if node:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
            del node
            
    def findNode(self,index, flag=False):
        cur = self.head.next
        ctr = 0
        while cur != self.tail:
            if ctr == index:
                return cur
            ctr += 1
            cur=cur.next
        if ctr == index and flag:
            return cur
        
        return None

    def display(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.val)
            cur=cur.next
