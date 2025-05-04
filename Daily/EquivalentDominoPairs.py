from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        seen = [0] * 100
        equalPairs = 0
        for a, b in dominoes:
            val = a * 10 + b if a <= b else a + b * 10
            equalPairs += seen[val]
            seen[val] += 1
        return equalPairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:       
        # Raw UnOptimised Solution
        seen = {}
        res = 0
        for domino in dominoes:
            domino.sort()

        for d in dominoes:
            check = (d[0], d[1])
            if check not in seen:
                seen[check] = 1
            else:
                seen[check] += 1

        for n in seen.values():
            res += (n * (n - 1)) // 2
        return res

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Brute Force -> TLE
        n = len(dominoes)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (
                    dominoes[j][0] == dominoes[i][1]
                    and dominoes[j][1] == dominoes[i][0]
                ) or (
                    dominoes[j][1] == dominoes[i][1]
                    and dominoes[j][0] == dominoes[i][0]
                ):
                    res += 1
        return res
