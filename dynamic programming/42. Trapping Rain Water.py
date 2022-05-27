"""

Hard

18592

261

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height:List[int]) -> int:
        n = len(height)
        left_max, right_max, left,right = 0,0, 0, n-1
        output = 0
        
        while left <= right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    output += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    output += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return output
    
    
    
    def trap_2n(self, height: List[int]) -> int:
        n = len(height)
        maax = -1
        mins = [-1]*n
        for i in range(n):
            maax = mins[i] = max(maax, height[i])
        maax = -1
        output = 0
        
        for i in range(n-1, -1, -1):
            maax = max(height[i], maax)
            output += min(mins[i], maax) - height[i]
            
        return output
            
