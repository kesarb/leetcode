"""

https://leetcode.com/problems/insert-interval/


57. Insert Interval
Medium

4373

321

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""


class Solution:

    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out_put = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                out_put.append(newInterval)
                out_put.extend(intervals[i:])
                return out_put
            elif newInterval[0] > intervals[i][1]:
                out_put.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        out_put.append(newInterval)
        return out_put



    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out_put = []
        if len(intervals) == 0:
            return [newInterval]
        new_start = newInterval[0]
        new_end = newInterval[1]
        flag = True
        found_position = False

        for i, j in intervals:
            if flag and new_end < i:
                out_put.append((new_start, new_end))
                flag = False
                out_put.append((i,j))
            elif flag and ( i <= new_start <= j or i <= new_end <=j or new_start <= i <=new_end or new_start <= j <= new_end):
                new_start = min(i, new_start)
                new_end = max(j, new_end)
            else:
                out_put.append((i,j))
        if flag:
            out_put.append((new_start, new_end))
        return out_put
