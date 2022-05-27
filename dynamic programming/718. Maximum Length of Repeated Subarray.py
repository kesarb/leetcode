"""
718. Maximum Length of Repeated Subarray
Medium

3842

93

Add to List

Share
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        
        m = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == nums2[i]:
                    dp[i+1][j+1] = dp[i][j]+1
                    m = max(dp[i+1][j+1],m)
        return m
