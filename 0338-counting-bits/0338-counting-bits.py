class Solution:
    def countBits(self, n: int) -> List[int]:
        def binaryRepr(n):
            binary = []
            
            while n != 0:
                if n % 2:
                    binary.append("1")
                else:
                    binary.append("0")
                
                n//=2
            
            return binary.count("1")
        
        ans = []
        for i in range(n+1):
            ans.append(binaryRepr(i))

        return ans


