"""
2035. Partition Array Into Two Arrays to Minimize Sum Difference
Hard

713

45

Add to List

Share
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
 

Constraints:

1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107
"""

class Solution:
    def find_lower_bound(self, target, arr):
        i = 0 
        j = len(arr)-1
        res = float('-inf')
        while i <= j:
            m = i+(j-i)//2
            if arr[m] <= target:
                i = m+1
                res = arr[m]
            else:
                j = m-1
        return res
    
    def minimumDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        N =len(nums)//2
        res  = float('inf')
        d1 = [set() for _ in range(N+1)]
        d1[0].add(0)
        
        d2 = [set() for _ in range(N+1)]
        d2[0].add(0)
        
        for index in range(N):
            num = nums[index]
            new = [set() for _ in range(N+1)]
            for idx in range(N):
                for i in d1[idx]:
                    new[idx+1].add(i+num)
            for i in range(1,N+1):
                d1[i].update(new[i])
        
        for index in range(N, len(nums)):
            num = nums[index]
            new = [set() for _ in range(N+1)]
            for idx in range(N):
                for i in d2[idx]:
                    new[idx+1].add(i+num)
            for i in range(1,N+1):
                d2[i].update(new[i])
        
        for i in range(N+1):
            x1 = list(d1[i])
            x2 = list(d2[N-i])
            if len(x1) < len(x2):
                x1,x2 = x2, x1
            x2.sort()
            for t in x1:
                r = self.find_lower_bound(total_sum//2-t, x2)
                res = min(res, abs(total_sum-2*(r+t)))
        
        return res
        
