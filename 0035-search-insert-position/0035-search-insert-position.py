class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = -1
        right = size

        while left + 1 != right:
            mid = left + (right-left)//2

            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        
        return right