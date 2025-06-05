from typing import List
import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x, y in points:
            d = sqrt(x**2 + y**2)
            heap.append([d,x,y])
        
        heapq.heapify(heap)
        res = []

        while k > 0:
            d, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
        return res
            
            
        