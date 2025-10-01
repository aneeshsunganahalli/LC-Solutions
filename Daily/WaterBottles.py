class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        res = numBottles
        while numBottles >= numExchange:
            left = numBottles % numExchange
            refill = numBottles // numExchange
            res += refill
            numBottles = refill + left
        return res
