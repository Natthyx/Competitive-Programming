class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        even_prefix = [0] * (n + 1)
        odd_prefix = [0] * (n + 1)
        
        for i in range(n):
            even_prefix[i + 1] = even_prefix[i]
            odd_prefix[i + 1] = odd_prefix[i]
            if i % 2 == 0:
                even_prefix[i + 1] += nums[i]
            else:
                odd_prefix[i + 1] += nums[i]
        
        count = 0
        
        for i in range(n):
            even_sum = even_prefix[i] + (odd_prefix[n] - odd_prefix[i + 1])
            odd_sum = odd_prefix[i] + (even_prefix[n] - even_prefix[i + 1])
            
            if even_sum == odd_sum:
                count += 1
        
        return count
