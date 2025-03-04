class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0]-x[1]) , reverse = True)

        n = len(costs)//2
        count_a = 0
        count_b = 0
        ans = 0

        for cost in costs:
            if cost[0] < cost[1]:
                if count_a < n:
                    ans+=cost[0]
                    count_a+=1
                else:
                    ans+=cost[1]
                    count_b+=1

                
            else:
                if count_b < n:
                    ans+=cost[1]
                    count_b+=1
                else:
                    ans+=cost[0]
                    count_a+=1

        return ans
                
