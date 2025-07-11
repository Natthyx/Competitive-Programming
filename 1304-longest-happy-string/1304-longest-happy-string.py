class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        counter = {
            "a": a,
            "b": b,
            "c": c
        }

        for key , val in counter.items():
            if val != 0:
                heappush(max_heap, (-val, key))
        
        res = ""

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)

            if len(res) > 1 and res[-1] == res[-2] == char1:
                if not max_heap:
                    break
                count2 , char2 = heapq.heappop(max_heap)

                res += char2
                count2 += 1

                if count2:
                    heapq.heappush(max_heap, (count2,char2))
            else:
                res += char1
                count1 += 1
            
            if count1:
                heapq.heappush(max_heap, (count1, char1))
        return res
