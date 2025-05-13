class Solution:
    def countBits(self, n: int) -> List[int]:
        def binaryRepr(n):
            count = 0
            
            while n != 0:
                if n % 2:
                    count+=1
                n//=2
            
            return count
        
        ans = []
        for i in range(n+1):
            ans.append(binaryRepr(i))

        return ans


