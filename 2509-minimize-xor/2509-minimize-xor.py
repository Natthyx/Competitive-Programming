class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        nm1 , nm2 = num1.bit_count() , num2.bit_count()

        ans = num1
        i = 0

        while nm1 > nm2:
            if ans & (1 << i):
                nm1 -= 1
                ans = ans ^ (1 << i)
            i+=1
        
        while nm1 < nm2:
            if ans & (1 << i ) == 0:
                nm1 += 1
                ans = ans | (1 << i)
            i+=1
        
        return ans
