class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        count =  Counter(stones)
        
        jewels = list(jewels)
        
        for i in jewels:
            if i in count:
                res += count[i]
                
        return res
        