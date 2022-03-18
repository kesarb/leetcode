"""
1053. Previous Permutation With One Swap
Medium

202

22

Add to List

Share
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.

 

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 104

"""

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # traverse the array from last to first
        # if decresing order break index
        # if index == -1 retun same array
        # swap the index and last possible element in the remaining array
        
        index = -1
        l1 = len(arr)
        prev = float('inf')
        for i in range(l1-1,-1, -1):
            if prev < arr[i]:
                index = i
                break
            prev =arr[i]
        
        if index == -1:
            return arr
        
        i = l1-1
        
        while arr[index] <= arr[i]:
            i -= 1
        while i != 0 and arr[i] == arr[i-1] :
            i -= 1
            
        arr[index], arr[i] = arr[i], arr[index]
        return arr
