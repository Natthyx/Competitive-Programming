class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mx = len(nums)
        req_prefix = [0]*(mx+1)

        for start, end in requests:
            req_prefix[start]+=1
            req_prefix[end+1]-=1

        for i in range(1, len(req_prefix)):
            req_prefix[i] += req_prefix[i-1]

        print(req_prefix)
        
        nums.sort(reverse=True)
        req_prefix.sort(reverse=True)
        
        for i in range(len(nums)):
            nums[i] = nums[i]*req_prefix[i]

        return sum(nums)% ((10**9) +7)
        


        



        
        


        



        