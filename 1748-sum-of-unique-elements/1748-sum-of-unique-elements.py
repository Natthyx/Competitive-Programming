class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for key, value in counter.items():
            if value == 1:
                res+=key
        return res