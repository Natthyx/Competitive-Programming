class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i],cost[i]))
        
        arr.sort()
        cst = 0
        curr = 0
        prefix = []
        for num in range(len(arr)):
            curr += ((arr[num][0]-arr[num-1][0])*cst)
            cst += arr[num][1]
            prefix.append(curr)

        suffix = []
        cst = 0
        curr = 0
        arr = arr[::-1]
        for num in range(len(arr)):
            curr += ((arr[num][0]-arr[num-1][0])*cst)
            cst += arr[num][1]
            suffix.append(abs(curr))

        suffix = suffix[::-1]
        mn = float('inf')
        for i in range(len(prefix)):
            mn = min(mn,(prefix[i]+suffix[i]))

        return mn