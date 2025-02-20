class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        suffixsum = [0] * 1001
        maxi = 0
        
        for num_passengers, start, end in trips:
            suffixsum[start] += num_passengers
            suffixsum[end] -= num_passengers
            maxi = max(maxi, end)
        
        if suffixsum[0] > capacity:
            return False
        
        for i in range(1, maxi + 1):
            suffixsum[i] += suffixsum[i - 1]
            if suffixsum[i] > capacity:
                return False
        
        return True