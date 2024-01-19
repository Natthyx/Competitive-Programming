class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        sum_costs = 0
        
        for i in costs:
            sum_costs +=i
            if sum_costs <= coins:
                count+=1
        return count
            
        