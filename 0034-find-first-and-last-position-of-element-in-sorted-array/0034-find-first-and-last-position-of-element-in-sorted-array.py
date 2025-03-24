class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        first , last = -1, -1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                first = mid
                r = mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                last = mid
                l = mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1

        
        return [first,last]

        
            

