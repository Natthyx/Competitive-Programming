class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                k = abs(x-y)
                heapq.heappush(stones,-k)
        
        if len(stones) == 0:
            return 0
        return -stones[0]


