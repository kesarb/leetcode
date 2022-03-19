import random
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.arr = []
        self.ctr = 0

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = self.ctr
            self.ctr += 1
            self.arr.append(val)
            return True
        
        return False
            

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        index = self.d[val]
        self.arr[index] = self.arr[-1]
        self.d[self.arr[index]] = index
        self.arr.pop()
        self.ctr -= 1
       
        
        del self.d[val]
        return True

    def getRandom(self) -> int:
        
        return self.arr[random.randint(0, self.ctr-1)]

