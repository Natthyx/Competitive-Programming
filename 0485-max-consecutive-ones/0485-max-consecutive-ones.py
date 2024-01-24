class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        ones = 0
        maxP = 0
        
        for right in range(len(nums)):
            if nums[right]==1:
                ones+=1
            
            while left <= right and nums[right] == 0:
                left = right + 1
            maxP = max(right-left+1,maxP)
                
        return maxP
                
                
                
                