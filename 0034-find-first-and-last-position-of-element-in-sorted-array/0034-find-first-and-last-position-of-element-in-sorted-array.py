class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(leftbiases):
            left = 0
            right = len(nums)-1
            res = -1

            while left <= right:
                mid = (left+right)//2

                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    res = mid
                    if leftbiases:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res
        
        first = binarySearch(True)
        last = binarySearch(False)
        return [first,last]





