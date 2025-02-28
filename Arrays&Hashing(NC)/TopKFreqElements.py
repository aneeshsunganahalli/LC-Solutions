from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:        # Creating the counter
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        heap = []
        for num in count.keys():  # Pushing into minHeap, using value as primary criterion
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:     # Only k top values stay in heap
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # Appending the value of each (key,value) pair
        
        return res