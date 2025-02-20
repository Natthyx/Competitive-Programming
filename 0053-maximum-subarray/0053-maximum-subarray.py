class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = nums[0]
        mx = nums[0]

        for i in range(1,len(nums)):
            prefix+=nums[i]
            if nums[i] > prefix:
                prefix = nums[i]

            mx = max(mx,prefix)

        return mx

       





        