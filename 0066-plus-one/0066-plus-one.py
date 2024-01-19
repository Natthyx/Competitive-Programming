class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int(''.join(map(str,digits)))
        digit +=1
        
        
        digit = list(map(int,str(digit)))
        
        return digit
        