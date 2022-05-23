class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def find2sum(start, total):
            #print(nums[start:], target)
            i = start
            j = len(nums)-1
            res = []
            while i<j:
                if i>start and nums[i]==nums[i-1]:
                    i+=1
                    continue
                if total == nums[i]+nums[j]:
                    res.append([nums[i], nums[j]])
                    i+=1
                    j-=1
                    
                    
                elif total > nums[i]+nums[j]:
                    i+=1
                else:
                    j-=1
            #print(res)
            return res
        
        def ksum(k, start, total_sum, elements):
            if k == 2:
                #print("before")
                r = find2sum(start, total_sum)
                if r:         
                    for each in r:
                        res.append(elements.copy())
                        res[-1].append(each[0])
                        res[-1].append(each[1])
                return
            
            for i in range(start, len(nums)-k+1):
                if i>start and nums[i] == nums[i-1]:
                    continue
                elements.append(nums[i])
                ksum(k-1, i+1, total_sum-nums[i], elements)
                elements.pop()
            
        ksum(3, 0, 0, [])
        return res
    
    
            
            
        
