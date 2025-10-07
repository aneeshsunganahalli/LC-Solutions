from typing import List
from collections import defaultdict
# 1488
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        full = defaultdict(int)
        res = []
        dry = []
        for r in range(len(rains)):
            if rains[r] > 0:
                if rains[r] not in full:
                    full[rains[r]] = r
                    res.append(-1)
                else:
                    x = full[rains[r]]
                    if dry:
                        s = dry[0]
                        if x < s < r:
                            res.append(s)
                            full[rains[r]] = r
                            dry.pop(0)
                    else:
                        return []
            else:
                dry.append(r)
        return res

                
        