class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0,46342):
            if 2**i == n:
                return True
            elif 2**i > n:
                break

        return False