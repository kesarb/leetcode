"""
1272. Remove Interval
Medium

A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]

Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

 

Constraints:

    1 <= intervals.length <= 104
    -109 <= ai < bi <= 109

"""

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        out_put = []
        i = 0
        output = []
        
        while i < len(intervals):
            
            value = intervals[i]
            if value[0] > toBeRemoved[1]:
                output.extend(intervals[i:])
                return output
            elif value[1] < toBeRemoved[0]:
                output.append(value)
            else:
                start = toBeRemoved[0]
                end = toBeRemoved[1]
                
                if value[0] < start < value[1]:
                    output.append([value[0],start])
                    
                if start == value[0] and end < value[1] or value[0] < end < value[1]:
                    output.append([end, value[1]])
                
            i += 1
        return output
