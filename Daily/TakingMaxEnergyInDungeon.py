from typing import List
# 3147
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        n = len(energy)
        prefix = [0] * n

        for i in reversed(range(n)):
            if i + k >= n:
                prefix[i] = energy[i]
            else:
                prefix[i] = energy[i] + prefix[i + k]
        return max(prefix)
      
      