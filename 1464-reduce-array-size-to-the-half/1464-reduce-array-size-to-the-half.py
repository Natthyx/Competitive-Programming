class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
 
        
        values = list(freq.values())
        values.sort(reverse=True)
        sm = 0
        count = 0

        for val in range(len(values)):
            sm += values[val]
            count+=1
            if sm >= len(arr)//2:
                break

        return count
            


        



        
