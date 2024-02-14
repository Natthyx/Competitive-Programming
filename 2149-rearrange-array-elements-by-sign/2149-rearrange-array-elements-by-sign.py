class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []
        
        for i in range(len(nums)):
            if nums[i]< 0 :
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
            
        return res