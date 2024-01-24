class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        self.N = len(nums)
        
        sm = 0
        
        for i in range(self.N):
            sm+=nums[i]
            self.prefix.append(sm)
       
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)