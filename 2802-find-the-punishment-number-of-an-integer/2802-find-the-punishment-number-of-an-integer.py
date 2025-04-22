class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        def checker(ind, curr , target, s):
            if ind == len(s) and curr == target:
                return True
            
            for i in range(ind,len(s)):
                if checker(i+1, curr + int(s[ind:i+1]) , target , s):
                    return True
            return False

        for i in range(1, n+1):
            if checker(0, 0 , i , str(i*i)):
                res += i * i
        
        return res