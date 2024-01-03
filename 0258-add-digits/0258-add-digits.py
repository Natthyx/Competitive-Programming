class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            output = (int(x) for x in str(num))
            sum_of = sum(j for j in output)
            num = sum_of
        return num
        