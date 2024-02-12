class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        res = []
        n = len(nums)
        
        for i in range(n):
            counter[nums[i]]+=1
        
        for key, value in counter.items():
            if value > (n/3):
                res.append(key)
        return res