class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        goodSub = {0:-1}
        curSum = 0
        
        
        for n in range(len(nums)):
            curSum += nums[n]
            r = curSum % k
            if r not in goodSub:
                goodSub[r] = n
            elif n - goodSub[r] > 1:
                return True
            
            
       
        
        
            
        