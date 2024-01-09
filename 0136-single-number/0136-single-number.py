class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            count = nums.count(i)
            if count == 1:
                return i
        