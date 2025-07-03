class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        max_heap = []


        for key, val in counter.items():
            heapq.heappush(max_heap, (-val,key))
        
        ans = []
        while k > 0 and max_heap:
            val , num = heapq.heappop(max_heap)

            ans.append(num)
            k-=1
        
        return ans



