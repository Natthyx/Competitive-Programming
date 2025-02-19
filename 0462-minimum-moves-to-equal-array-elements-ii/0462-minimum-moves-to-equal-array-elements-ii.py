class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = len(nums)//2

        sm = 0
        for i in range(len(nums)):
            sm += abs(nums[target]-nums[i])


        return sm