from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        
        count = Counter(s)
        oddMax, evenMin = 0, max(count.values())
        for c in count.values():
            if c % 2 == 0 and c < evenMin:
                evenMin = c
            if c % 2 == 1 and c > oddMax:
                oddMax = c
        return oddMax - evenMin