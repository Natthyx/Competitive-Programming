class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = [[-1]*2 for _ in range(len(prices))]

        def dp(i,hold):
            if i >= len(prices):
                return 0
            if memo[i][hold] != -1:
                return memo[i][hold]

            if hold:
                sell = dp(i+1, 0) + prices[i] - fee
                holding = dp(i+1, 1)
                memo[i][hold] = max(sell, holding)
            else:
                buy = dp(i+1, 1) - prices[i]
                skip = dp(i+1,0)
                memo[i][hold] = max(buy,skip)


            
            return memo[i][hold]
        
        return dp(0,0)