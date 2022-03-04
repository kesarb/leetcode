"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        dect = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen", 
                15: "Fifteen", 
                16: "Sixteen",  
                17: "Seventeen", 
                18: "Eighteen", 
                19: "Nineteen", 
                20: "Twenty",
                30: "Thirty",
                40: "Forty",
                50: "Fifty",
                60: "Sixty",
                70: "Seventy",
                80: "Eighty",
                90: "Ninety",
                100: "Hundred",
                1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
            }
        
        def num2eng(num):
            if num ==0:
                return ""
            
            d = {2: 100, 3: 1000, 6: 1000000, 9: 1000000000}
            
            i = 9
            tens =[9,6,3,2]
            index = -1
            for i in tens:
                if num // (10**i) != 0:
                    index = i
                    break
            
            left_part = num // (10**index)
            right_part = num % (10**index)
            output = ""
            if index in d:
                output = num2eng(left_part) +" " + dect[d[index]]
                
            
            if (index == -1):
                if num in dect:
                    output = output +" " + dect[num]
                else:
                    twos = (num //10) *10
                    ones = num%10
                    
                    output = output +  " "+ dect[twos] +" "+ dect[ones]    
            else:
                output = output +" "+ num2eng(right_part)
            return output.strip()
            
        return num2eng(num)
