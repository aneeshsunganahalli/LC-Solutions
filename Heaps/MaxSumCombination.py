# Maximum Sum Combinations

# You are given two integer arrays a[] and b[] of equal size. A sum combination is formed by adding one element from a[] and one from b[], using each index pair (i, j) at most once. Return the top k maximum sum combinations, sorted in non-increasing order.

# Examples:

# Input: a[] = [3, 2], b[] = [1, 4], k = 2
# Output: [7, 6]
# Explanation: Possible sums: 3 + 1 = 4, 3 + 4 = 7, 2 + 1 = 3, 2 + 4 = 6, Top 2 sums are 7 and 6.

# Input: a[] = [1, 4, 2, 3], b[] = [2, 5, 1, 6], k = 3
# Output: [10, 9, 9]
# Explanation: The top 3 maximum possible sums are : 4 + 6 = 10, 3 + 6 = 9, and 4 + 5 = 9

import heapq
class Solution:
    def topKSumPairs(self, a, b, k):
        
        
        a.sort()
        b.sort()
        
        seen = set()
        seen.add((0,0))
        n = len(a)
        
        max_heap = [( -(a[n - 1] + b[n - 1]), n - 1, n - 1)]
        
    
        res = []
        
        for _ in range(k):
            neg_sum, i, j = heapq.heappop(max_heap)
            
            res.append(-neg_sum)
            
            if i - 1 >= 0 and (i - 1, j) not in seen:
                first = a[i - 1] + b[j]
                heapq.heappush(max_heap, (-first, i - 1, j))
                seen.add((i - 1, j))
            
            if j - 1 >= 0 and (i, j - 1) not in seen:
                second = a[i] + b[j - 1]
                heapq.heappush(max_heap, (-second, i, j - 1))
                seen.add((i, j - 1))
        
        return res  