class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        
        while i < n:
            if nums[i] and nums[i] != i + 1:
                ind = nums[i] - 1
                nums[i] , nums[ind] = nums[ind] , nums[i]
            else:
                i+=1
 
        for i in range(n):
            if nums[i]==0:
                return i+1

        return 0