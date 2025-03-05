class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R, L = 0 , 0
        ans = 0

        for letter in s:
            if letter == "R":
                R+=1
            else:
                L+=1
            if R == L:
                ans+=1
                R = 0
                L = 0
        
        return ans
