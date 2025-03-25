from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles] # x1 and x2
        y = [(r[1], r[3]) for r in rectangles] # y1 and y2

        x.sort()
        y.sort()

        def nonOverlapCount(intervals): # Classic way to check if intervals are overlapping
            count = 0
            prevEnd = -1 
            for start, end in intervals:
                if prevEnd <= start:
                    count += 1
                prevEnd = max(end, prevEnd)
            return count


        return max(
            nonOverlapCount(x), # We just need to know if we can get 3 non overlapping intervals in any way
            nonOverlapCount(y)
        ) >= 3