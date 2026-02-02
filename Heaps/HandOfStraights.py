# 846
from heapq import heapify, heappop
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapify(min_heap)

        while min_heap:
            start = min_heap[0]
            for x in range(start, start + groupSize):
                if count[x] == 0:
                    return False
                count[x] -= 1
                if count[x] == 0:
                    if x != min_heap[0]:
                        return False
                    heappop(min_heap)
        return True


        # Greedy (Not most optimal though due to repeated pushbacks)
        if len(hand) % groupSize != 0:
            return False

        heapify(hand)

        while hand:
            rem = groupSize
            temp = []
            first = heappop(hand)
            rem -= 1
            prev = first
            while rem > 0 and hand:
                val = heappop(hand)
                if val == prev + 1:
                    rem -= 1
                    prev += 1
                else:
                    temp.append(val)

            if rem != 0:
                return False
            for item in temp:
                heappush(hand, item)
        return True


        