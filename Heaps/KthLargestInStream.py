from heapq import heappush, heappop
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums,k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
        