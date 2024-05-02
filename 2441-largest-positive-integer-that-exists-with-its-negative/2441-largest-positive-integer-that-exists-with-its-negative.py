class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if -i in nums:
                res.append(i)
        
        if len(res) == 0:
            return -1
        else:
            return max(res)
                
        