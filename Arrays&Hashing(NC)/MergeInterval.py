from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort by starting times
        intervals.sort(key=lambda x: x[0])
        # Start with first interval, merge if overlap, else just add current interval
        # Merge occurs only to the most recently appended interval in res
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = res[-1]  # Points to reference, doesn't copy value
            curr = intervals[i]

            if prev[1] < curr[0]:   # No Overlap
                res.append(curr)

            else:   # Overlap, so merge 
                prev[1] = max(prev[1], curr[1])

        return res
