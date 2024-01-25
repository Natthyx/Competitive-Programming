class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curSum = 0
        res = 0
        prefix = {0:1}
        for i in range(len(nums)):
            curSum += nums[i]
            nums[i]=curSum
        for i in range(len(nums)):
            mod = nums[i] % k
            res+=prefix.get(mod,0)
            prefix[mod]=prefix.get(mod,0)+1
        return res

    