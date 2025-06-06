from typing import List
import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # Represents smaller elements, maxHeap
        self.large = [] # Represents larger elements, minHeap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large): # we maintain len(large) > len(small)
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))    
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num)) # Intuitive

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            maxOfSmall = -self.small[0]
            minOfLarge = self.large[0]
            return (maxOfSmall + minOfLarge) / 2
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()