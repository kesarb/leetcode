"""
215. Kth Largest Element in an Array
Medium

8546

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
def findKthLargest(self, nums: List[int], k: int) -> int:   
        k = len(nums)-k
        #print(k)
        def kselect(start, end):
            pivot = nums[end]
            j = start
            for i in range(start,end):
                if pivot > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[j], nums[end] = pivot, nums[j]
            #print(start, end, j)
            if j == k:
                return nums[j]
            
            if j < k:
                return kselect(j+1, end)
            return kselect(start, j-1)
        
        return kselect(0,len(nums)-1)
