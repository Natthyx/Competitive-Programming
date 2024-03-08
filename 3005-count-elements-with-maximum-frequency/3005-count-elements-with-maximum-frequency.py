class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        res = 0
        for key,value in count.items():
            if value == max(count.values()):
                res +=value
        return res
            