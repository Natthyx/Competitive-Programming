class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            ind = nums[i] - 1
            if nums[ind] != nums[i]:
                nums[ind],nums[i] = nums[i], nums[ind]
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]-1 != i:
                res.append(nums[i])

        return res
