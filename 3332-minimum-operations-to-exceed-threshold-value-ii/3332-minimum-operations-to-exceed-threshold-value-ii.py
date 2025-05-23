class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        while len(nums) >= 2:
            if nums[0] >= k:
                return count
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            count+=1

            sm = min(x,y)*2 + max(x,y)

            heapq.heappush(nums,sm)
            

        
        return count
