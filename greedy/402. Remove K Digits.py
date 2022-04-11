"""
402. Remove K Digits
Medium

5951

247

Add to List

Share
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

class Solution:
    def removeKdigits_timelimit_exceed(self, num: str, k: int) -> str:
        # 
        #pass
        if num == "0":
            return "0"
        
        while k >0 and num:
            if len(num) > 1 and num[1] == '0':
                k-=1
                num = num[1:]
                while num and num[0]=='0':
                    num = num[1:]
                continue
                    
            prev = 0
            for index in range(1, len(num)):
                if num[prev] <= num[index]:
                    prev = index
                else:
                    break
            num = num[:prev]+num[prev+1:]
            k-=1
            #print(k)
            
        return "0" if num == "" else num
    
    def removeKdigits(self, nums: str, k: int) -> str:
        
        stack = []
        flagzero = False
        
        for ch in nums:
            while stack and k>0 and stack[-1]>ch:
                stack.pop()
                k-=1
            stack.append(ch)
        
        res = stack[:len(stack)-k]
        res="".join(res)
        res= res.lstrip("0")
        
        return res if res else "0"
                
        
        
