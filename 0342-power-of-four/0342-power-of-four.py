class Solution:
    def power(self,n):
        if n == 1:
            return True
        if n % 4 == 0:
            n//=4
            return self.power(n)
        else:
            return False
            
        
        
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        ans = self.power(n)
        return ans
            