from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastOccur = {} # Hash Map to figure last index of all characters

        for i, c in enumerate(s):
            lastOccur[c] = i
        
        res = []
        start = 0 # Two Pointers
        end = 0

        for i, c in enumerate(s): 
            end = max(end, lastOccur[c])

            if end == i:  # Currently at last index of all chars in substring, so append length
                res.append(end - start + 1)
                start = i + 1
        return res