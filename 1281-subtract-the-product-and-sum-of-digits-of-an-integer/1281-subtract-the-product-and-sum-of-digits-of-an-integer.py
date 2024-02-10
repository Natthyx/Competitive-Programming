class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(str(n))
        sm = 0
        ml = 1
        for i in lst:
            temp = int(i)
            sm+=temp
            ml*=temp
            
        res = ml - sm
        return res
            