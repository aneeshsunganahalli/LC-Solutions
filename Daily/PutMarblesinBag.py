from typing import List
import heapq

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        # Sorting Solution
        if k == 1:
            return 0

        splits = [] # Array which stores the sum of the boundaries of every possible partition in the weights array
        for i in range(len(weights) - 1):
            splits.append(weights[i] + weights[i+1])
        
        splits.sort() # Sort so we can take the k-1 smallest and k-1 biggest sums for the min and max scores 

        p = k - 1
        maxScore = sum(splits[-p:])
        minScore = sum(splits[:p])

        return maxScore - minScore

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # My Slow Heap Solution
        if k == 1:
            return 0

        splitsMinHeap = []
        splitsMaxHeap = []

        for i in range(len(weights) - 1):
            heapq.heappush(splitsMinHeap, weights[i] + weights[i+1])
            heapq.heappush(splitsMaxHeap, -(weights[i] + weights[i+1]))

        maxScore, minScore = 0,0
        
        while k - 1 > 0:
            minScore += heapq.heappop(splitsMinHeap)
            maxScore += -(heapq.heappop(splitsMaxHeap))
            k -= 1
        
        return maxScore - minScore