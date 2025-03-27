class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if max(nums)==0:
            return 0
        def decrement(k):
            diff= [0]*(len(nums)+1)
            for i in range(k+1):
                l,r,val = queries[i]
                diff[l] -= val
                diff[r+1] += val
            
            sm= 0
            for i in range(len(nums)):
                sm+=diff[i]
                if nums[i] + sm > 0:
                    return False
            return True

        
        l, r = 0, len(queries)-1

        while l <= r:
            mid = (l+r)//2
            if decrement(mid):
                r = mid-1
            else:
                l = mid+1


        return l+1 if l < len(queries) else -1
            

        