class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        counter = []
        for i in range(len(nums)):
            counter.append([nums[i],i])
        
        counter.sort()
        while l < r:
            if counter[l][0]+counter[r][0] == target:
                return [counter[l][1],counter[r][1]]
            elif counter[l][0]+counter[r][0] > target:
                r-=1
            else:
                l+=1

       
