class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        digits = []
        for c in s:
            if not c.isdigit():
                break
            digits.append(c)
        
        if not digits:
            return 0
        num = int(''.join(digits)) * sign
        
        num = max(min(num, 2**31 - 1), -2**31)
        
        return num