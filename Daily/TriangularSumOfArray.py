class Solution:
    def triangularSum(self, nums) -> int:

        while len(nums) > 1:
            newNums = []
            for i in range(1, len(nums)):
                newNums.append((nums[i] + nums[i - 1]) % 10)
            nums = newNums
        return nums[0]
