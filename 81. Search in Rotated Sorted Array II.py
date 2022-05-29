"""
81. Search in Rotated Sorted Array II

Duplicate
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[end]:
                end = end-1
                continue
            
            if nums[mid]<nums[end]:
                if nums[mid]<target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if nums[start]<=target<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return False 
                    
                
                
            
