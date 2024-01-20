class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1  
        i, j = 1, 1

        while j < len(nums):
            if nums[j] == nums[j - 1]:
                count += 1
            else:
                count = 1  

            if count <= 2:
                nums[i] = nums[j]
                i += 1

            j += 1

        return i
                
        