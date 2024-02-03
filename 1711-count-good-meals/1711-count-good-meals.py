class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        frequency = defaultdict(int)

        for num in deliciousness:
            for i in range(22): 
                target = 2**i - num
                count += frequency[target]

            frequency[num] += 1

        return count % ((10**9) + 7)   
                
                
            
            