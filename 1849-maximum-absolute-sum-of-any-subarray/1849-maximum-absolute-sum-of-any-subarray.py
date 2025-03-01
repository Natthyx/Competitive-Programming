class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefixsm = nums[0]
        mx = nums[0]
        prefixm = nums[0]
        mn = nums[0]

        for i in range(1,n):
            prefixsm = max(prefixsm+nums[i], nums[i])
            prefixm = min(prefixm+nums[i], nums[i])
            mn = min(mn,prefixm)
            mx = max(mx,prefixsm)


        return max(mx,abs(mn))






            
            
        