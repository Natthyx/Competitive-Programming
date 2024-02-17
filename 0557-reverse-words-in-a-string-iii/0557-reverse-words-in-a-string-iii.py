class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        r = []
        
        for i in range(len(s)):
            rev = s[i][::-1]
            r.append(rev)
            
        res = " ".join(r)
        return res
        
        
        
            
            