class Solution:
    def isThree(self, n: int) -> bool:
        count = 1
        for i in range(2,n+1):
            if n%i==0:
                count +=1
        if count == 3:
            return True
        