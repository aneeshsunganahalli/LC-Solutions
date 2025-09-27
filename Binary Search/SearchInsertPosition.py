class Solution:
    def searchInsert(self, nums, target: int) -> int:

        low = 0
        high = len(nums) - 1
        res = 0

        # If target not present, look for largest element smaller than target
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                res = max(res,mid + 1)
                low = mid + 1
        return res
