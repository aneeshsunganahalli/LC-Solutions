# 451
class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        arr = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for k,v in arr:
            res += k * v
        return res