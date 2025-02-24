class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        ans = [0] * n
        
        prefix[0] = 0 
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        suffix[n - 1] = 0  
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        for i in range(n):
            left_count = i  
            right_count = n - i - 1 
            
            left_sum = left_count * nums[i] - prefix[i]
            right_sum = suffix[i] - right_count * nums[i]

            ans[i] = left_sum + right_sum

        return ans


