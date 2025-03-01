class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mn , mx = 0 , 0
        sm = 0

        for i in range(len(nums)):
            sm += nums[i]
            if sm > mx:
                mx = sm
            if sm < mn:
                mn = sm


        return abs(mx-mn)
        