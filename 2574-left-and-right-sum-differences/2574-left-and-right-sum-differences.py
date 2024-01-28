class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefixrev = [0] * len(nums)
        res = []

        for i in range(len(nums)):
            if i-1<0:
                continue
            prefix[i] = nums[i-1]+prefix[i-1]

        for i in range(len(nums)-1,-1,-1):
            if i+1==len(nums):
                continue
            prefixrev[i] = nums[i+1] + prefixrev[i+1]
        for i in range(len(nums)):
            temp = abs(prefix[i] - prefixrev[i])
            res.append(temp)

        return res



        