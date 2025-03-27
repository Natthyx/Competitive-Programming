class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        def checker(k,h):
            total = sum(math.ceil(p/k) for p in piles)
            return total<= h
        ans = r
        while l <= r:
            mid = (l+r)//2
            if checker(mid,h):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        
        return ans






            