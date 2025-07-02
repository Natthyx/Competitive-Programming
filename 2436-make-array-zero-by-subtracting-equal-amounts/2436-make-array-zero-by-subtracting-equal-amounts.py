class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        while nums and nums[0] == 0:
            heapq.heappop(nums)
        count = 0

        while nums:
            if nums[0] == 0:
                heapq.heappop(nums)
                continue
            else:
                x = heapq.heappop(nums)

                for i in range(len(nums)):
                    nums[i] -= x
                
                count += 1

        
        return count