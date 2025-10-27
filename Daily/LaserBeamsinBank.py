# 2125
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        # Optimal
        res = prev = 0
        for row in bank:
            cams = row.count('1')
            if cams > 0:
                res += cams * prev
                prev = cams
        return res


        # Initial Solution
        def count(string):
            val = 0
            for c in string:
                val += int(c)
            return val
        
        nums = []
        for row in bank:
            if count(row) != 0:
                nums.append(count(row))
        res = 0
        for i in range(len(nums) - 1):
            res += nums[i] * nums[i + 1]
        return res