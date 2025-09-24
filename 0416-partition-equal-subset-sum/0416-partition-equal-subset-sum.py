class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        target = sum(nums) // 2
        if sum(nums) % 2:
            return False

        def dp(i,curr):
            if curr == target:
                return True
            
            if i >= len(nums) or curr > target:
                return False
            
            if (i,curr) in memo:
                return memo[(i,curr)]

            memo[(i,curr)] = dp(i+1, curr + nums[i]) or dp(i+1, curr)

            return memo[(i,curr)]

        return dp(0,0)
