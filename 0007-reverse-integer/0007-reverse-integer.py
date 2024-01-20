class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        ans = 0
        x = abs(x)

        while x > 0:
            ans = (ans * 10) + (x % 10)
            x //= 10
        
        if flag:
            ans = -ans
        
        return ans if (-2**31) <= ans <= (2**31 - 1) else 0