class Solution:
    def findGCD(self, nums: List[int]) -> int:
        arr= []
        nums.sort()
        for i in range(1, nums[-1]+1):
            if nums[0] % i == 0 and (nums[-1])%i==0:
                arr.append(i)   
        return arr[-1]
            
            
        