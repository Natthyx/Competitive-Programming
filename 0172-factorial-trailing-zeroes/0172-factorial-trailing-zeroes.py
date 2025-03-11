class Solution:
    def factorial(self, num):
            if num == 0:
                return 0
            
            k = factorial(num-1)
            return num * k
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        ans = self.factorial(n)
        count = 0


        while ans > 0:
            if ans%10 == 0:
                count+=1
                ans= ans // 10
            else:
                break

        return count


        