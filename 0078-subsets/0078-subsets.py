class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]] 
        for num in nums:
            result += [current + [num] for current in result]
        return result
        
        