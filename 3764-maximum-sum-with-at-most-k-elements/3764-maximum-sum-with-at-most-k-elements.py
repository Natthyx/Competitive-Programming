class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                heap.append([-grid[i][j], i])

        heapq.heapify(heap)
        ans = 0
        while k > 0:
            num = heapq.heappop(heap)

            if limits[num[1]] > 0:
                k-=1
                limits[num[1]]-=1
                ans += -num[0]

        return ans

        