class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1,n+1):
            left = sum(range(1,i+1))
            right = sum(range(i,n+1))
            if left == right:
                return i
        return -1
            
        