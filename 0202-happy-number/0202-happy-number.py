class Solution:
    def isHappy(self, n: int) -> bool:
        seen_sum = set()
        while n!=1:
            output = [int(i) for i in str(n)]
            sumof = sum(j**2 for j in output)
            n = sumof
            if n in seen_sum:
                return False
            seen_sum.add(n)
        return True
            
            
            
        