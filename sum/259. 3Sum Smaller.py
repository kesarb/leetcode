"""
259. 3Sum Smaller
Medium

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:

Input: nums = [], target = 0
Output: 0

Example 3:

Input: nums = [0], target = 0
Output: 0

 

Constraints:

    n == nums.length
    0 <= n <= 3500
    -100 <= nums[i] <= 100
    -100 <= target <= 100


"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #nums = list(zip(nums, range(len(nums))))
        nums.sort()
        def sum2(start, _target):
            i = start
            j = len(nums)-1
            r = 0
            while i<j:
                su = nums[i]+nums[j]
                if su < _target:
                    r += j-i
                    i+=1
                else:
                    j-=1
            return r
        
        s = 0
        for idx in range(len(nums)):
            s += sum2(idx+1, target-nums[idx])
        return s
