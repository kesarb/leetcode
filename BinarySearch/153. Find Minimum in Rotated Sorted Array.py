class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        
        while (end-start)>1:
            mid = start+(end-start)//2
            if nums[mid]<nums[end]:
                end = mid
            else:
                start = mid
                
        return min(nums[start], nums[end])
    
    
