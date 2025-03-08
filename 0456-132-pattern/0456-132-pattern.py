class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mx_stack = []
        mn = [float("inf")]*len(nums)

        for i in range(1,len(nums)):
            mn[i] = min(mn[i-1],nums[i-1])

        
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > mn[j]:
                while mx_stack and mx_stack[-1] <= mn[j]:
                    mx_stack.pop()
                
                if mx_stack and mx_stack[-1] < nums[j]:
                    return True
                mx_stack.append(nums[j])
            
        return False