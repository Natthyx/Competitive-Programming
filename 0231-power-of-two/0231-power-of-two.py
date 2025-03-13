class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if int(n) == 0:
            return False
        if int(n) == 1: 
            return True
        if n % 2 == 1:
            return False
        
        return self.isPowerOfTwo(n/2)