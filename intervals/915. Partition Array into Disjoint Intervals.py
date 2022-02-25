"""
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Constraints:

2 <= nums.length <= 105
0 <= nums[i] <= 106
There is at least one valid answer for the given input.
"""

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        l = len(nums)
        suffix_min = [0]*l 
        prefix_max = [0]*l
        min_s = float('inf')
        max_s = float('-inf')
        for i in range(l):
            min_s = suffix_min[l-i-1] = min(nums[l-i-1], min_s)
            max_s= prefix_max[i] = max(nums[i], max_s)
        for i in range(l-1):
            if prefix_max[i] <= suffix_min[i+1]:
                return i+1
        
        
