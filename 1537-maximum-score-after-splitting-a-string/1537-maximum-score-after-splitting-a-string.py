class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        zeros_arr = []
        mx = 0
        ones_arr = s.copy()
        
        for i in range(len(s)-1):
            zeros_arr.append(s[i])
            ones_arr.remove(s[i])
            mx = max(mx, (zeros_arr.count("0")+ones_arr.count("1")))

        
        return mx
            
