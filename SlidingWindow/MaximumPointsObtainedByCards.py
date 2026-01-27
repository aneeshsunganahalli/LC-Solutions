# 1423
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        total = sum(cardPoints[n - k:])

        res = total
        for i in range(k):

            total += cardPoints[i]
            total -= cardPoints[n - k + i]

            res = max(res, total)
        return res