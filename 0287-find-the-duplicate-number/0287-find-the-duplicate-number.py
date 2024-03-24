class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        
        for key, value in count.items():
            if value > 1:
                return key
            
         