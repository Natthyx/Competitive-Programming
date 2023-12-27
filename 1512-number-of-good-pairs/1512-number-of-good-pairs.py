class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i]==nums[j] and i<j:
                    arr.append((i,j))         
        return len(arr)
                    
        