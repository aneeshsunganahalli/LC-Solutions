class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split(".")
        v2 = version2.split(".")

        n = max(len(v1), len(v2))
        
        for i in range(n):
            c1 = int(v1[i]) if i < len(v1) and v1[i] != "" else 0
            c2 = int(v2[i]) if i < len(v2) and v2[i] != "" else 0

            if c1 > c2:
                return 1
            if c1 < c2:
                return -1
        return 0
            