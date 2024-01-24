class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # prefixsum = [nums[0]]
        # sum = 0
        
        # for i in range(1,len(nums)):
            # prefixsum.append(nums[i] + prefixsum[i-1])
        
        prefixsum = []
        sum = 0
        
        for i in nums:
            sum+=i
            prefixsum.append(sum)
        return prefixsum
