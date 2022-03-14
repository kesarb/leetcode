"""
2099. Find Subsequence of Length K With the Largest Sum
Easy

363

28

Add to List

Share
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""
import heapq
class Solution:
    def maxSubsequence1(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        for i,j in enumerate(nums):
            list1.append((j,i))
            
        list1.sort()  
        list1 = list1[len(nums)-k:]
        list1.sort(key= lambda x: x[1])
        
        return [i for i,j in list1]
    
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        #max heap
        
        heap = []
        
        for i,j in enumerate(nums):
            
            if len(heap) >= k:
                if heap[0][0] <= j:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (j,i))
            else:
                heapq.heappush(heap, (j,i))
            
            #print(heap)
        heap.sort(key = lambda x: x[1])
        return [i for i,j in heap]      
        
        
