# 2654
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n, ones = len(nums), 0
        g = 0

        def gcd(m, n):
            while n != 0:
                temp = m % n
                m = n
                n = temp
            return m

        for num in nums:
            if num == 1:
                ones += 1
            g = gcd(g , num)

        if ones > 0:
            return n - ones
        if g > 1:
            return -1

        res = n
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i + 1)
                    break
        
        return res + n - 2