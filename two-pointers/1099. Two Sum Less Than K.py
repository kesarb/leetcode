"""
1099. Two Sum Less Than K

Easy

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 1000
    1 <= k <= 2000




"""

class Solution:
    def twoSumLessThanK1(self, nums: List[int], k: int) -> int:
        
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tmp = nums[i] + nums[j]
                if  tmp < k and res < tmp:
                    res = tmp
        return res
    
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        count = [0] * (1001)
        
        
        res = -1
        m = -1
        for i in nums:
            if k > i:
                count[i] = 1
            m = max(m, i)
            
        i = 0
        j = m
        res = -1
        while i < j:
            if count[i] and count[j]:
                if i+j < k:
                    res = max(res, i+j)
                if i+j >= k:
                    j -= 1
                else:
                    i += 1
                continue
            if count[i] == 0:
                i+=1 
            if count[j] == 0:
                j -= 1
            
        
        return res
    
