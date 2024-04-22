class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a,2)
        num2 = int(b,2)
        result = num1 + num2
        
        return bin(result)[2:]