class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1001
        mx = 0
        mn = float("inf")
        for num, begin, des in trips:
    
            prefix[begin]+= num
            prefix[des]-= num
            mx = max(mx,des)
        if prefix[0] > capacity:
            return False
        for i in range(1,mx+1):
            prefix[i] += prefix[i-1]
            if prefix[i] > capacity:
                return False

        return True
           

        