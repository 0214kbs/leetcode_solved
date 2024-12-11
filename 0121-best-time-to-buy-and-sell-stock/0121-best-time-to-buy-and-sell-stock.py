class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minv = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            price = prices[i]
            if minv < price:
                max_profit = max(price-minv, max_profit)
            else:
                minv = price
        return max_profit