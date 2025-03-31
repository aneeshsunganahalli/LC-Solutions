from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minP = float('inf')
        maxP = 0
        for price in prices:
            if minP > price:
                minP = price
            profit = price - minP

            if maxP < profit:
                maxP = profit
        return maxP

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        r =  1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            else:
                res = max(res, profit)
            r += 1
        return res