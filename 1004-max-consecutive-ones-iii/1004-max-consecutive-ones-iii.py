class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxP = 0
        ones = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                ones+=1
            while (right-left+1)-ones > k:
                if nums[left] == 1:
                    ones-=1
                left+=1
            maxP = max(maxP,right-left+1)
        return maxP
                
        