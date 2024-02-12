class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = []
        counter = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            if nums[i]%2 == 0:
                counter[nums[i]]+=1
        if not bool(counter):
            return -1
        max_value = max(counter.values())
        for key,value in counter.items():
            if value == max_value:
                res.append(key)
        return min(res)
                
                
            
        