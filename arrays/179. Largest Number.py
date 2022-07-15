"""
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        @cmp_to_key
        def cmp (a,b):
            if int(str(a)+str(b)) > int(str(b)+str(a)):
                return -1
            else:
                return 0
                
        nums.sort(key=cmp)
        num = list(map(str, nums))
        y = "".join([str(i) for i in nums]).lstrip('0')
        if not y:
            y = "0"
        return y
