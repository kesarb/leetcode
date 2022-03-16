"""
705. Design HashSet
Easy

1209

152

Add to List

Share
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""

class MyHashSet:

    def __init__(self):
        self.hash_size = 100
        self.hash = [set() for i in range(self.hash_size) ]
        self.count = 0
        
    def resize(self):
        
        self.hash_size = self.hash_size*100
        newhash =  [set() for i in range(self.hash_size) ]
        for lst in self.hash:
            for i in lst:
                newhash[i%self.hash_size].add(i)
            lst.clear()
        self.hash.clear()
        self.hash = newhash
   
    def shrink(self):
        self.hash_size //= 100
        newhash =  [set() for i in range(self.hash_size) ]
        for lst in self.hash:
            for i in lst:
                newhash[i%self.hash_size].add(i)
            lst.clear()
        self.hash.clear()
        self.hash = newhash
        
        
    def add(self, key: int) -> None:
        if self.count == self.hash_size:
            self.resize()
            
        if len(self.hash[key%self.hash_size]) == 0:
            self.count += 1
            
        self.hash[key%self.hash_size].add(key)

    def remove(self, key: int) -> None:
        
        lst = self.hash[key%self.hash_size]
        if lst and key in lst:
            lst.remove(key)
            if len(lst) == 0:
                self.count -= 1
                
        if self.count > 100 and self.count < self.hash_size//100:
            self.shrink()
            
    def contains(self, key: int) -> bool:
        lst = self.hash[key%self.hash_size]
        if lst and key in lst:
            return True
        return False
