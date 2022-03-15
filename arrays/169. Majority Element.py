"""
169. Majority Element
Easy

9017

326

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        current_max = nums[0]
        current_count = 1
        i = 1
        while i < len(nums):
            if nums[i] == current_max:
                current_count+=1
            else:
                if current_count != 0:
                    current_count  -= 1
                else:
                    current_max = nums[i]
                    current_count += 1
            i += 1
        return current_max
    
