"""
You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.
"""
class Solution:
    def aggressiveCows(self, stalls, k):
        
        stalls.sort() # Have to sort for this function to work since the logic depends on it to count number of possible cows
        def possible(distance: int) -> bool:
            
            cowCount = 1
            last = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last >= distance:
                    last = stalls[i]
                    cowCount += 1
            if cowCount >= k:
                return True
            return False
        
        lo = 1
        hi = max(stalls) - min(stalls)
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if possible(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi