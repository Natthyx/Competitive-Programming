class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l , r = 0 , 10**9
        houses.sort()
        heaters.sort()

        def checker(radius):
            i, j = 0 , 0

            while i < len(houses) and j < len(heaters):
                if heaters[j] - radius <= houses[i] <= heaters[j] + radius:
                    i+=1
                else:
                    j+=1
            
            if i == len(houses):
                return True
            else:
                return False
        while l <= r:
            mid = (l+r)//2

            if checker(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l