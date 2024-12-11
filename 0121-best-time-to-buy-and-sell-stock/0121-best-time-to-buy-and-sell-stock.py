class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minv = prices[0]
        check = [0 for _ in range(len(prices))]
        for i in range(len(prices)):
            price = prices[i]
            if minv < price:
                check[i] = price-minv
            else:
                minv = price
        return max(check)
