class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        iterate from left to right
        - If the current number nums[i] is smaller than the max seen so far, it means this
         number is out of order, so the right boundary must include i.
        - If the current number is bigger than max_seen, we update max_seen.

        iterate from right to left
        - If the current number nums[i] is bigger than the min seen so far, it is out of 
         order, so the left boundary must include i.
        - If the current number is smaller than min_seen, we update min_seen.

        - If right == -1, it means the array is already sorted → return 0.
        - Otherwise, the length of the unsorted subarray is right - left + 1.
        '''
        right = -1
        max_seen = float("-inf")
        for i in range(len(nums)):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]
        
        left = -1
        min_seen = float("inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]
        
        return 0 if right == -1 else right - left + 1