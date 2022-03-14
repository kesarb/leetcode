"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
  """

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        max1 = float("-inf")
        for index, val in enumerate(nums):
            for j in range(index):
                if nums[j] < val:
                    lis[index] = max(lis[index], 1+lis[j])
            max1 = max(lis[index], max1)
        return max1
    
    def lengthOfLIS_subsequencedp(self, nums: List[int]) -> int:
        nums1 = list(nums)
        nums.sort()
        nums2 = nums
        
        l1 = len(nums1)
        l2 = len(nums2)
        dp = [[0 for i in range(l1+1)] for j in range(l2+1)]
        
        prev = None
        for i in range(1,l2+1):
            if prev == nums2[i-1]:
                for j in range(l1+1):
                    dp[i][j] = dp[i-1][j]
                continue
            prev = nums2[i-1]
            for j in range(1, l1+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[l2][l1]
        
        
