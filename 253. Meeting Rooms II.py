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
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        max1 = 1
        intervals.sort()
        intervals = [[j,i] for i, j in intervals]
        min_heap = []
        for each in intervals:
            while min_heap and each[1] >= min_heap[0][0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, each)
            max1 = max(max1, len(min_heap))

        return max1
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
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
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
