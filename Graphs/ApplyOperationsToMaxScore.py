from typing import List
from heapq import heapify, heappop
import heapq
from math import sqrt

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        # Convert inputs into prime scores
        primeScores = []
        for n in nums:
            score = 0
            for f in range(2 ,int(sqrt(n) + 1 )):
                if n % f  == 0:
                    score += 1
                    while n % f == 0:
                        n  = n // f
            if n >= 2:
                score += 1
            primeScores.append(score)

        # Monotonic Stack
        leftBound = [-1] * N
        rightBound = [N] * N

        stack = []
        for i, s in enumerate(primeScores):
            while stack and primeScores[stack[-1]] < s:
                index = stack.pop()
                rightBound[index]  = i
            if stack:
                leftBound[i] = stack[-1]
            stack.append(i)

        minHeap = [(-n,i) for i, n in enumerate(nums)]
        heapify(minHeap)

        while k > 0:
            n, index = heapq.heappop(minHeap)
            n = -n
            score = primeScores[index]

            leftCount = index  - leftBound[index]
            rightCount = rightBound[index] - index

            count = leftCount * rightCount
            operations = min(count,k)
            res = (res * pow(n,operations, MOD)) % MOD
            k -= operations
        return res