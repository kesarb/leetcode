"""
658. Find K Closest Elements
Medium

6389

522

Add to List

Share
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

#neet
class Solution:
    def findClosestElements(self, arr: List[int], k: int, target: int) -> List[int]:
        l = 0
        r = len(arr)-k
        if k== len(arr):
            return arr
        while l < r:
            mid = l+(r-l)//2
            
            if target-arr[mid] > arr[mid+k] - target:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]
