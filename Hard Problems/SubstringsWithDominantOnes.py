# 3234

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        res, N = 0, len(s)
        next_zero = [N] * N
        for i in range(N-2, -1, -1):
            if s[i + 1] == '0':
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]
        
        for l in range(N):
            zeros = 1 if s[l] == '0' else 0
            r = l

            while zeros * zeros <= N:
                next_z = next_zero[r]
                ones = next_z - l - zeros
                if ones >= zeros * zeros:
                    res += min (
                        next_z - r,
                        ones - zeros * zeros + 1
                    )
                r = next_z
                zeros += 1
                if r == N:
                    break
        return res