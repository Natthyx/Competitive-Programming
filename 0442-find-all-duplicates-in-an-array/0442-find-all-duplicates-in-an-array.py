class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate = defaultdict(int)
        res = []
        for num in nums:
            duplicate[num]+=1
        
        for key,value in duplicate.items():
            if value == 2:
                res.append(key)
                
        return res