class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        counter = Counter(nums)

        for key , val in counter.items():
            if val == 1:
                res+=key
        
        return res

