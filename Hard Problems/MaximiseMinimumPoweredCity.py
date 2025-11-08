# 2528
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
        N = len(stations)
        diff = [0] * (N + 1)
        for i in range(N):
            left = max(i - r, 0)
            right = min(i + r + 1, N)

            diff[left] += stations[i]
            diff[right] -= stations[i]

        def can_achieve(target_p):
            diff_copy = diff.copy()
            cur_k = k
            cur_p = 0
            for i in range(N):
                cur_p += diff_copy[i]
                if cur_p < target_p:
                    additional = target_p - cur_p
                    if additional > cur_k:
                        return False
                    cur_k -= additional
                    cur_p += additional
                    right = min(N, i + 2*r + 1)
                    diff_copy[right] -= additional
            return True
        
        low, high = min(stations), sum(stations) + k
        res = low
        while low <= high:
            target = (low + high) // 2
            if can_achieve(target):
                res = target
                low = target + 1
            else:
                high = target - 1
        return res