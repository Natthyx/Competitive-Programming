class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        cons_shift = [0]*n
        sm = 0
        res = ''
        
        
        for start, end , di in shifts:
            if di ==1:
                cons_shift[start]+=1
                if end+1<n:
                    cons_shift[end+1]-=1
            else:
                cons_shift[start]-=1
                if end+1<n:
                    cons_shift[end+1]+=1
        for i in range(len(cons_shift)):
            sm+=cons_shift[i]
            cons_shift[i]=sm
        
        alph = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(s)):
            cons_shift[i] +=alph.index(s[i])
        for i in range(len(cons_shift)):
            a = cons_shift[i] % 26
            res+=alph[a]
            
        return res
            
        
            
            
            
            
        
        
                
        