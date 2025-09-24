class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = []

        if (numerator  < 0) ^ (denominator < 0):
            res.append("-")
        
        numerator , denominator = abs(numerator) , abs(denominator)
        
        res.append(str(numerator // denominator))
        
        remainder = numerator % denominator

        if not remainder:
            return "".join(res)
        
        res.append(".")

        hash_map = {}

        while remainder:
            if remainder in hash_map:
                res.insert(hash_map[remainder] , "(")
                res.append(")")
                break
            
            hash_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder//denominator))
            remainder %= denominator
        

        return "".join(res)