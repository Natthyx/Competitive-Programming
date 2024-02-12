class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = defaultdict(int)
        
        for i in range(n):
            counter[nums[i]]+=1
        for key, value in counter.items():
            if value > (n/2):
                return key
            
            
        
        
        
            