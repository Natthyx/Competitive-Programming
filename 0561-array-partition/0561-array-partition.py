class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = sum(nums[i] for i in range(0, len(nums), 2))
        return result
        