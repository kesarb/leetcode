"""
347. Top K Frequent Elements
Medium

7652

333

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq
from collections import defaultdict
class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) - 1
        heap = [(val,i) for i, val in dic.items()]
        heapq.heapify(heap)
        i = k
        res = []
        while i > 0:
            res.append(heapq.heappop(heap)[1])
            i-=1
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
            
        res = [[] for i in range(len(nums)+1)]
        
        for i, val in dic.items():
            res[val].append(i)
            
        i = len(nums)
        output = []
        while i > 0:
            for j in res[i]:
                output.append(j)
                if len(output) == k:
                    return output
            i -= 1
        
