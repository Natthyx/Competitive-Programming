class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum = 1
        for d in range(2,int(num ** 0.5)+1):
            if num%d == 0:
                sum +=d + num//d
        return sum == num
        
                
        