class Solution:        

    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        
       
        for i in range(n-1):
            new_s = s + "1"
            s = list(s)
            for i in range(len(s)):
                s[i] = "1" if s[i] == "0" else "0"
            s = s[::-1]

            new_s += "".join(s)
            s = new_s
            
        return s[k-1]




        
        
