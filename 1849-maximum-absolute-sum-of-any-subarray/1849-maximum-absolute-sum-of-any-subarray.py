class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefixsm = nums[0]
        mx = nums[0]

        for i in range(1,n):
            prefixsm = max(prefixsm+nums[i], nums[i])

            mx = max(mx,prefixsm)

        
        prefixm = nums[0]
        mn = nums[0]

        for i in range(1,n):
            prefixm = min(prefixm+nums[i], nums[i])
            mn = min(mn,prefixm)


        return max(mx,abs(mn))






            
            
        