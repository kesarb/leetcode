"""
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Medium

12277

489

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution:
    def addNum(self, newInterval) -> None:
        out_put = []
        for i in range(len(self.interavals)):
            if newInterval[1] < self.interavals[i][0]:
                out_put.append(newInterval)
                out_put.extend(self.interavals[i:])
                self.interavals = out_put
                return
            elif newInterval[0] > self.interavals[i][1]:
                out_put.append(self.interavals[i])
            else:
                newInterval = [min(self.interavals[i][0], newInterval[0]), max(self.interavals[i][1], newInterval[1])]

        out_put.append(newInterval)
        self.interavals = out_put
    
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        self.interavals = []
        for i in intervals:
            self.addNum(i)
        return self.interavals
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        i = 1
        
        for start, end in intervals:
            
            t1, t2 = output[-1]
            
            if t2 >= start:
                output[-1] = [min(t1, start), max(t2, end)]
            else:
                output.append((start, end))
                
        return output
            
        
