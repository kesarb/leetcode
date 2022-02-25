"""
1288. Remove Covered Intervals
Medium

1812

44

Add to List

Share
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 1
        output = []
        for start, end in intervals:
            if len(output) > 0:
                t1, t2 = output[-1]
                if t1 <= start <= end <= t2 or start <= t1 <= t2 <= end:
                    output[-1] = [min(t1, start), max(t2, end)]
                    continue
            output.append((start, end))
                
        return len(output)
