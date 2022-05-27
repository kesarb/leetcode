"""

Medium

7511

118

Add to List

Share
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    def canPartitionm(self, nums: List[int]) -> bool:
        dp =  set()
        su = sum(nums)
        if su%2:
            return False
        su = su//2
        dp.add(0)
        for each in nums:
            nd = set()
            for t1 in dp:
                ns = t1+each
                if ns <= su:
                    if ns == su:
                        return True
                    nd.add(ns)
            dp.update(nd)
        #print(dp)
        return False
    
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su%2:
            return False
        su = su//2
        
        @cache
        def rec(s, index):
            if s > su:
                return False
            if s == su:
                return True
            if index >= len(nums):
                return False
            
            if not rec(s, index+1):
                return rec(s+nums[index], index+1)
            return True
        
        return rec(0, 0)
            
