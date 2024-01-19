class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left,right+1):
            ch=True
            num = str(i)
            for j in num:
                if j == "0" or i% int(j)!=0:
                    ch= False
            if ch:
                arr.append(i)
        return arr

        