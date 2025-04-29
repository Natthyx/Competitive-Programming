class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()
        targetInd = None
        for i in range(len(times)):
            if times[i] == target:
                targetInd = i
                break

        heap = []
        heapq.heapify(heap)
        chairs = [i for i in range(len(times)+1)]
        heapq.heapify(chairs)
        
        for i,(start,end) in enumerate(times):
            start , end = times[i]
            while heap and start >= heap[0][0]:
                _ , sitInd = heapq.heappop(heap)
                heapq.heappush(chairs,sitInd)
                
            sit = heapq.heappop(chairs)
            heapq.heappush(heap,(end,sit))

            if i == targetInd:
                return sit