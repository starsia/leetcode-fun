class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if (prices[i] < curr):
                curr = prices[i]
            elif (prices[i] - curr > max_profit):
                max_profit = prices[i] - curr

        return max_profit
