class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        # First, find the first element from the right that is smaller than the element next to it.
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        # If such an element was found, then we can form the next permutation
        if pivot != -1:
            # Now, we find the smallest element greater than the 'pivot', starting from the end
            for j in range(len(nums)-1,pivot,-1):
                if nums[j] > nums[pivot]:
                    nums[j] , nums[pivot] = nums[pivot] , nums[j]
                    break
        
        nums[pivot+1:] = nums[pivot+1:][::-1]

        