class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        
        ascii_num = []
        
        for i in s:
            ascii_num.append(ord(i))
        
        
        i , j = 0, 1
        
        while j < len(ascii_num):
            res += abs(ascii_num[i]-ascii_num[j])
            i+=1
            j+=1
            
        return res
        