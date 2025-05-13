class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def ones(n):
            count = 0
            while n != 0:
                if n % 2:
                    count+=1
                n//=2
            return count

        k = x^y
        return ones(k)