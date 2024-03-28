class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        ans, start = 0 , -1
        
        for end in range(len(nums)):
            frequency[nums[end]]+=1
            
            while frequency[nums[end]] > k:
                start+=1
                frequency[nums[start]] -=1
            ans = max(ans , end - start)
        return ans