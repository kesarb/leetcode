"""
45. Jump Game II
Medium

7583

284

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        end = 0
        n = len(nums)
        m_so_far = 0
        for i in range(n-1):
            m_so_far = max(m_so_far, i+nums[i])
            if end == i:
                end = m_so_far
                res+=1
                
        return res
        
        return res
    def jump(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)
        num_os_steps = nums[i]
        
        while i < n-1:
            j = 1
            m_so_far = i+num_os_steps
            while j <= num_os_steps and i+j < n:
                m_so_far = max(m_so_far, nums[i+j]+i+j)
                j += 1
                
            res += 1
            old = num_os_steps
            num_os_steps = m_so_far-(i+num_os_steps)
            i = i+old
        return res

            
