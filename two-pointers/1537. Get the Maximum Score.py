"""
1537. Get the Maximum Score
Hard

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
The score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].
Example 2:

Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
Output: 109
Explanation: Maximum sum is obtained with the path [1,3,5,100].
Example 3:

Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
Output: 40
Explanation: There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 107
nums1 and nums2 are strictly increasing.
"""

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        i =0
        j = 0
        res = 0
        sum1 = 0
        sum2 = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1+= nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                res += nums1[i] + max(sum1, sum2)
                sum1 = 0
                sum2 = 0
                i+=1
                j+=1
        
        res += max(sum1+sum(nums1[i:]), sum2+sum(nums2[j:])) 
        return res% (10**9 + 7)
        
        
