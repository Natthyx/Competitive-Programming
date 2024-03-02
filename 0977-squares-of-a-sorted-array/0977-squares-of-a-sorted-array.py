class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            sqr = nums[i] ** 2
            res.append(sqr)
        res.sort()
        return res
        