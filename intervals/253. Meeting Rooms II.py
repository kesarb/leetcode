'''
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

 

Constraints:

    1 <= intervals.length <= 104
    0 <= starti < endi <= 106

'''

import heapq
class Solution:
    def minMeetingRooms_heap(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        rooms = 0
        
        for start, end in intervals:
            while heap and heap[0][0] <= start:
                heapq.heappop(heap)
                
            heapq.heappush(heap, (end,start))
            rooms = max(len(heap), rooms)
        return rooms
       
       
    def minMeetingRooms_two_array(self, intervals: List[List[int]]) -> int:
        start = [i for i,j in intervals]
        end = [j for i, j in intervals]
        start.sort()
        end.sort()
        j = 0
        i = 0
        ctr = 0
        minimum = 1
        while i < len(start):
            if start[i] < end[j]:
                ctr += 1
                i += 1
                minimum = max(ctr, minimum)
            else:
                j += 1
                ctr -= 1
        return minimum
    
    
    #more efficiency 
    def minMeetingRooms_sortarray(self, intervals: List[List[int]]) -> int:
        ctr = 0
        expand  = []
        for i, j in intervals:
            expand.append((i,1))
            expand.append((j,-1))
        expand.sort()
        minimum = 0
        for i,j in expand:
            ctr += j
            minimum = max(ctr, minimum)
        return minimum

       
       
  
