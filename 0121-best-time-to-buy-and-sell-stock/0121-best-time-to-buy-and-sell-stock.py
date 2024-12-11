class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minv = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            price = prices[i]
            if minv > price:
                minv = price
                continue
            if price-minv > max_profit:
                
                max_profit = price-minv
        return max_profit