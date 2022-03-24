class MyCircularQueue:

    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.queue = [-1]*k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.rear == -1:
            self.rear = self. front = 0
        else:
            self.rear +=1
        self.rear %= self.k    
        self.queue[self.rear]= value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        ele = self.queue[self.front]
        
        if self.rear== self.front:
            self.front = self.rear = -1
        
        else:
            self.front += 1
            self.front %= self.k
        return True
        
           
        
    def Front(self) -> int:
        if not self.isEmpty():
            ele = self.queue[self.front]
            return ele
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            ele = self.queue[self.rear]
            return ele
        return -1

    def isEmpty(self) -> bool:
        if self.front == -1 and self.front == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == (self.rear+1) % self.k:
            return True
        return False
