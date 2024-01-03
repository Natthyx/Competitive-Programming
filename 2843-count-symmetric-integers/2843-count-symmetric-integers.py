class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            string = str(i)
            if len(string)% 2 == 0:
                mid = len(string)//2
                sum_f = sum(int(digit) for digit in string[:mid])
                sum_m = sum(int(digit) for digit in string[mid:])
                if sum_f == sum_m:
                    count +=1
        return count
                    
            
                
        