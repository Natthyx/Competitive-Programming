class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        n = len(nums)-1
        mx = 0
        for i, num in enumerate(nums):
            mx = max(mx,num+i)
            if num == 0 and i >= mx:
                break

            elif i + num >= n:
                return True



        return False

        