class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxXOR = 0
        
        for x in nums:
            for y in nums:
                if abs(x-y) <= min(x,y):
                    xor = x ^ y
                    maxXOR = max(maxXOR,xor)
        
        
        return maxXOR
                
                
            
            
        