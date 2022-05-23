class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def sum2(start, _target):
            
            
            i = start
            j = len(nums)-1
            r = []
            while i<j:
                if start == i or nums[i] != nums[i-1]:
                    su = nums[i]+nums[j]
                    if su == _target:
                        r.append((nums[i], nums[j]))
                        i+=1
                        j-=1
                    elif su < _target:
                        i+=1
                    else:
                        j-=1
                else:
                    i+=1
            return r
                
        
        
        def ksum(k, start, _target, _res):
            if k < 2:
                return
            if k == 2:
                r = sum2(start, _target)
                for s1,s2 in r:
                    res.append(_res.copy())
                    res[-1].append(s1)
                    res[-1].append(s2)
                return
            
            for i in range(start, len(nums)):
                if start==i or nums[i] != nums[i-1]:
                    _res.append(nums[i])
                    ksum(k-1, i+1, _target - nums[i], _res)
                    _res.pop()
        
        ksum(4,0, target, [])
        return res
    
    
            
            
        
        
                
                
