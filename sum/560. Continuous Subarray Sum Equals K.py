"""
560. Subarray Sum Equals K
Medium

12348

390

Add to List

Share
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixsum = 0
        dic = {0:1}
        for i in nums:
            prefixsum += i
            count += dic.get(prefixsum - k, 0)
            dic[prefixsum] = 1 + dic.get(prefixsum,0)
        return count
