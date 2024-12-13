class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = prices[0]
        res = 0
        maxv = -1
        for pi in range(1, len(prices)):
            # print("============",pi, "============")
            # print('before',minv, maxv,res)
            if minv > prices[pi]:
                if maxv != -1:
                    res += maxv-minv
                minv = prices[pi]
                maxv = -1
            else:
                if maxv < prices[pi]:
                    maxv = prices[pi]
                else:
                    res += maxv-minv
                    minv = prices[pi]
                    maxv = -1
            # print('after',minv, maxv, res)
        if maxv == prices[-1]:
            res += maxv-minv
        return res