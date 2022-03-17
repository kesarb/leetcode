"""

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(start, end):
            if start>end:
                return None
                
            if start == end:
                return TreeNode(nums[start])
            
            mid = start+(end-start)//2
            
            root = TreeNode(nums[mid])
            root.left = rec(start, mid-1)
            root.right = rec(mid+1, end)
            
            return root
        
        return rec(0,len(nums)-1)
