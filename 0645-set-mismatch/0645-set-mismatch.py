class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                ind = nums[i]-1
                if nums[ind] == nums[i]:
                    i+=1
                else:
                    nums[ind] , nums[i] = nums[i] , nums[ind]
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
                res.append(i+1)

        return res    