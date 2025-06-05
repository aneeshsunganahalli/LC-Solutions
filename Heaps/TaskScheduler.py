from typing import List
import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks) # Counter for freq of each task
        maxHeap = [-c for c in count.values()] # Max Heap
        heapq.heapify(maxHeap)

        time = 0   # Starts at 0
        q = deque() # [-cnt, idleTime] format

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1] # Skip the idleTime, by setting time to next task's time
            else:
                cnt = 1 + heapq.heappop(maxHeap) # Essentially decreasing count by 1 in heap
                if cnt:
                    q.append([cnt, time + n]) # If count remains, set next task n cycles later in queue

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time