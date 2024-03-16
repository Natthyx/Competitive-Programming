class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        maxlen = 0
        count = 0

        for i in range(len(nums)):
            count = count + 1 if nums[i] == 1 else count - 1
            if count in hashmap:
                maxlen = max(maxlen, i - hashmap[count])
            else:
                hashmap[count] = i

        return maxlen