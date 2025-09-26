from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        

        # Merge Sort
        n = len(nums)

        # Before merging, check for pairs and store into count
        def countPairs(nums, low, mid, high):
            count = 0
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1
                count += right - (mid + 1)
            return count

        def merge(nums, l, mid, r):
            n1 = mid - l + 1
            n2 = r - mid

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = nums[l + i]
            for j in range(n2):
                R[j] = nums[mid + 1 + j]

            i = 0
            j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] > R[j]:
                    nums[k] = R[j]
                    j += 1
                else:
                    nums[k] = L[i]
                    i += 1
                k += 1

            while i < n1:
                nums[k] = L[i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = R[j]
                j += 1
                k += 1 

        def mergeSort(nums, l, r):
            count = 0
            if l >= r:
                return count

            mid = (l + r) // 2 
            count += mergeSort(nums, l, mid)
            count += mergeSort(nums, mid + 1, r)
            count += countPairs(nums, l, mid, r)
            merge(nums, l, mid, r)
            return count

        return mergeSort(nums, 0, n - 1)

        # Brute Force
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1,len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count