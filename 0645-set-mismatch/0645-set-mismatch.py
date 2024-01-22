class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        sumtoN = n*(n+1)//2
        missingNum = sumtoN - sum(set(nums))
        duplicateNum = sum(nums) - (sumtoN - missingNum)
        return [duplicateNum,missingNum]
            
            
            
        