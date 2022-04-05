"""
1993. Operations on Tree
Medium

205

36

Add to List

Share
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
The node is unlocked,
It has at least one locked descendant (by any user), and
It does not have any locked ancestors.
Implement the LockingTree class:

LockingTree(int[] parent) initializes the data structure with the parent array.
lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is possible, the node num will become locked by the user with id user.
unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it is possible, the node num will become unlocked.
upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it is possible, the node num will be upgraded.
"""

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.node = {}
        # childs
        # users
        
        for index, node in enumerate(parent):
            if node not in self.node:
                self.node[node] = {"children": [], "users":set()}
            if index not in self.node:
                self.node[index] = {"children": [], "users":set()}
            self.node[node]["children"].append(index)
        
    def lock(self, num: int, user: int) -> bool:
        #print(self.node)
        if not self.node[num]["users"]:
            self.node[num]["users"].add(user)
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if user in self.node[num]["users"]:
            self.node[num]["users"].remove(user)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        """
        The node is unlocked, - Done
        It has at least one locked descendant (by any user), and
        It does not have any locked ancestors.
        """
        if not self.node[num]["users"]:
            #It does not have any locked ancestors.
            index = num
            while index != -1:
                if self.node[self.parent[index]]["users"]:
                    return False
                index = self.parent[index]
            
            #It has at least one locked descendant (by any user), and
            #bfs
            queue = [num]
            flag = False
            while queue:
                n = queue.pop(0)
                if self.node[n]["users"]:
                    flag = True
                    self.node[n]["users"].clear()
                for each in self.node[n]["children"]:
                    queue.append(each)
            if flag:
                self.node[num]["users"].add(user)
            return flag
                
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
