"""
621. Task Scheduler

Share
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""

class Solution:
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            d[i]=d.get(i, 0)+1
        heap = [-1*d[i] for i in d]
        heapq.heapify(heap)
        queue = []
        
        timeStamp=0
        i = 0
        
        while heap or queue:
            timeStamp+=1
            if heap:
                p = heapq.heappop(heap)
                if p+1:
                    queue.append((timeStamp+n, p+1))
            if queue and queue[0][0] == timeStamp:
                    heapq.heappush(heap, queue.pop(0)[1])
        return timeStamp
                    
            
            
            
