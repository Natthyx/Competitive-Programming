class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moore-vomiting-algorithm

        candidate = 0
        count = 0

        for num in nums:
            # if count is zero, we will consider the current element as a candidate
            if count == 0:
                candidate = num
            # if current element same with candidate, we will increment the count by one, else decrement
            if num == candidate:
                count+=1
            else:
                count-=1
        # because it is guarantee that the element exists it will be one element left after all cancellation
        return candidate
