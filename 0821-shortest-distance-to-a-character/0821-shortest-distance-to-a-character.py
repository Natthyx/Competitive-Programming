class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float('inf')] * n 
        prev_char = float('-inf') 
        for i in range(n):
            if s[i] == c:
                prev_char = i
            res[i] = min(res[i], abs(i - prev_char))
        prev_char = float('inf') 
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev_char = i
            res[i] = min(res[i], abs(i - prev_char))
        
        return res