class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def checker(num):
            if citations[num] >= n - num:
                return True
            else:
                return False

        left , right = 0 , len(citations)-1
        ans = 0
        while left <= right:
            mid = (left+right)//2
            if checker(mid):
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1


        return ans