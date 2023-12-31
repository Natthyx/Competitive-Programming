class Solution:
    def romanToInt(self, s: str) -> int:
        num = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000 
        }
        sum_result = 0
        prev = 0
        for i in reversed(s):
            value = num[i]
            if  value < prev:
                sum_result -=value
            else:
                sum_result +=value
                prev = value
            
        return sum_result
        
        
        