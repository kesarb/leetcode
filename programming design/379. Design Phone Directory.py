"""
379. Design Phone Directory
Medium

Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, check if a certain slot is empty or not, and empty a given slot.

Implement the PhoneDirectory class:

    PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
    int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
    bool check(int number) Returns true if the slot number is available and false otherwise.
    void release(int number) Recycles or releases the slot number.

 

Example 1:

Input
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
Output
[null, 0, 1, true, 2, false, null, true]

Explanation
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
phoneDirectory.get();      // Assume it returns 1.
phoneDirectory.check(2);   // The number 2 is available, so return true.
phoneDirectory.get();      // It returns 2, the only number that is left.
phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
phoneDirectory.release(2); // Release number 2 back to the pool.
phoneDirectory.check(2);   // Number 2 is available again, return true.

"""

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.m_release = set()
        self.current = 0
        
    def get(self) -> int:
        if self.maxNumbers != self.current or self.m_release:
            if self.maxNumbers != self.current:
                res = self.current
                self.current+=1
                return res
            res = self.m_release.pop()
            return res
        return -1

    def check(self, number: int) -> bool:
        if (self.maxNumbers != self.current and self.current<=number ) or number in self.m_release:
            return True
        return False
    
    def release(self, number: int) -> None:
        if self.current>number and number not in self.m_release:
            self.m_release.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
