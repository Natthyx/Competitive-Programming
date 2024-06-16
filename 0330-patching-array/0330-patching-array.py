class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i,output,upto = 0,0,0
        
        while upto < n:
            if i < len(nums) and nums[i] <= upto+1:
                upto += nums[i]
                i+=1
            else:
                output+=1
                upto+=(upto+1)
        return output