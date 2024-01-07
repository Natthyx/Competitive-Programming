class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums) - 1
        # i = 0
        # step = 0
        # while step < k:
        #     nums[:] = [nums[n]] + nums[i:n]
        #     step += 1
        n = len(nums)
        k %= n  
        nums[:] = nums[n-k:] + nums[:n-k]
        
        
            