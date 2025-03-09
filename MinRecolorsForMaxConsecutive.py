# First Solution

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)

        i = 0
        j = k - 1
        minWhite = float('inf')

        while j < N:
            whiteCount = 0
            for c in range(i,j + 1):
                if blocks[c] == 'W':
                    whiteCount += 1
            minWhite = min(minWhite,whiteCount)
            i += 1
            j += 1

        return minWhite

# Optimised Solution

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        whiteCount = 0

        for i in range(0,k):
            if blocks[i] == 'W':
                whiteCount += 1
        
        minCount = whiteCount

        for i in range(k,N):
            if blocks[i-k] == 'W':
                whiteCount -= 1
            if blocks[i] == 'W':
                whiteCount += 1
            minCount = minCount if minCount < whiteCount else whiteCount

        return minCount
