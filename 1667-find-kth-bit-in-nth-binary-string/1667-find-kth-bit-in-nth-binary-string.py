class Solution:        
    def string(self,n):
        if n == 1:
            return "0"

        prev = self.string(n-1)
        reverse = ["1" if i == "0" else "0" for i in prev]
        ans = prev + "1" + "".join(reverse[::-1])
        return ans


    def findKthBit(self, n: int, k: int) -> str:
        return self.string(n)[k-1]

        
        




        
        
