class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ptr1 = 0
        ptr2 = len(nums)-1
        result = 0
        
        while ptr1<ptr2:
            if nums[ptr1]+nums[ptr2] == k:
                result+=1
                ptr1+=1
                ptr2-=1
            elif nums[ptr1]+nums[ptr2]<k:
                ptr1+=1
            else:
                ptr2-=1
        
        return result
            
        