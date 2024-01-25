class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        shift = [0]*n
        sm = 0
        res = ''
        left = 0
        for i in range(len(shifts)):
            shift[left] += shifts[i]
            if i+1< n:
                shift[i+1]-=shifts[i]
        for i in range(len(shift)):
            sm+=shift[i]
            shift[i]=sm
        alp = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(s)):
            shift[i] += alp.index(s[i])
        for i in range(len(shift)):
            a = shift[i]% 26
            res+=alp[a]
        return res
        
        
        
            
        