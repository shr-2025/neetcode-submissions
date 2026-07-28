class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0

        for p in prices:
            if p < min_val:
                min_val = p
            else:
                profit = max(profit, p - min_val)
        return profit
        