"""
215. Kth Largest Element in an Array
Medium

8555

478

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [ (x[0]**2+x[1]**2, index) for index, x in enumerate(points)]
        heapq.heapify(heap)
        i = k
        res = []
        while len(heap) and i > 0:
            x = heapq.heappop(heap)
            res.append(points[x[1]])
            i -= 1
        
        return res
