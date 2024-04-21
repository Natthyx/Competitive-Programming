class Solution(object):
    def addToArrayForm(self, num, k):
        my_int = int(''.join(map(str, num)))
        ans = my_int + k
        
        res = [int(nums) for nums in str(ans)]
        
        return res
        