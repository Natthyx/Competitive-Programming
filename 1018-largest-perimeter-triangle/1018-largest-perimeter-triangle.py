class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse= True)

        i , j = 0 ,  1

        for k in range(2,len(nums)):
            if nums[j] + nums[k] > nums[i]:
                sm = nums[i] + nums[j] + nums[k]
                return sm
            i+=1
            j+=1
        
        return 0
