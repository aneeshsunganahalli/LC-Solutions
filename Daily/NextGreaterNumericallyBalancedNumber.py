# 2048
from itertools import permutations
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        # Cheesy solution using permutations and manually writing possible combinations
        beautiful = set()
        valid = [ '1', '22', '122', '333', '1333', '4444', '14444','122333','1224444', '22333', '55555', '155555','224444', '666666']
        for num in valid:
            for p in permutations(num):
                beautiful.add(int (''.join(p)))
        for s in sorted(beautiful):
            if s > n:
                return s
        return -1

        # Similar approach with binary search
        def check(x):
            for num, count in Counter(str(x)).items():
                if num != str(count):
                    return False
            return True
        
        valid = []
        for i in range(1224445):
            if check(i):
                valid.append(i)
            
        lo, hi = 0, len(valid) - 1
        res = valid[-1]

        while lo <= hi:
            mid = (lo + hi) // 2
            if valid[mid] > n:
                res = valid[mid]
                hi = mid - 1
            else:
                lo = mid + 1
        return res



        # TLE in Python
        # Approach is to generate valid numbers, sort and look for the first one bigger than n
        # Biggest answer is 122444

        def isBeautiful(count):
            for d in range(1, 8):
                if count[d] != 0 and count[d] != d:
                    return False
            return True

        def generate(num, count, valid):
            if num > 0 and isBeautiful(count):
                valid.append(num)
            if num > 1224444:
                return
            
            for d in range(1,8):
                if count[d] < d:
                    count[d] += 1
                    generate(num * 10 + d, count, valid)
                    count[d] -= 1
        
        valid = []
        generate(0, [0] * 8, valid)
        valid.sort()
        for num in valid:
            if num > n:
                return num
        return -1
        
        