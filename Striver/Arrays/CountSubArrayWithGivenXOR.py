"""
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
"""
from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        
        # Main idea lies in with current XOR, to get k, we need some x such that x ^ k = XOR, we check for this x using x = k ^ XOR
        seen = defaultdict(int)
        seen[0] = 1
        xor = 0
        res = 0
        
        for i in range(len(arr)):
            xor ^= arr[i]
            x = xor ^ k

            res += seen[x]
            seen[xor] += 1 
              
        return res
            