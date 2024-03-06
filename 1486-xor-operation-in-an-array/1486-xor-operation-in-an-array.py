class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 1
        nums = []
        nums
        
        while i < n :
            temp = start + 2 * i
            nums.append(temp)
            i+=1
        
        res = start
        for num in nums:
            res = res ^ num
        return res
            
            
            