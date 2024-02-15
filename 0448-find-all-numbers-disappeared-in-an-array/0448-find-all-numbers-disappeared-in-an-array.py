class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        res= []
        nums.sort()
        n = len(nums)
        for i in nums:
            counter[i]+=1
        for i in range(1,n+1):
            if i not in counter:
                res.append(i)
                
        return res