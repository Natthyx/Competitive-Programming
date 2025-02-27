class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = []
        count = 0
        prefix_dict = defaultdict(int)
        
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count-=1
            else:
                count+=1
            prefix.append(count)

        for i in range(len(prefix)-1,-1,-1):
            prefix_dict[prefix[i]] = i
        prefix_dict[0] = -1
        
        for r in range(len(nums)):
            ans = max(ans, r - prefix_dict[prefix[r]])

        return ans
