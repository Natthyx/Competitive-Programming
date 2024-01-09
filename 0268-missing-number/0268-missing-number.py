class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = 0
        n = len(nums)
        for i in range(0,n+1):
            if i not in nums:
                arr+=i
        return arr
                
                

        
        
        