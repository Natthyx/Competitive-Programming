class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c**0.5)
        while i <= j:
            result = i**2 + j**2
            if result == c :
                return True
            elif result < c:
                i+=1
            else:
                j-=1
        return False

        
        