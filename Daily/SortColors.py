from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Dutch Flag Algo
        red, white, blue = 0, 1, 2

        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            x = nums[m]
            if x == red:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1
            elif x == white:
                m += 1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1




        # redCount, whiteCount, blueCount = 0,0,0
        # for num in nums:
        #     if num == 0:
        #         redCount += 1
        #     elif num == 1:
        #         whiteCount += 1
        #     else:
        #         blueCount += 1
        
        # i = 0
        # while redCount:
        #     nums[i] = 0
        #     i += 1
        #     redCount -= 1
        
        # while whiteCount:
        #     nums[i] = 1
        #     i += 1
        #     whiteCount -= 1
        
        # while blueCount:
        #     nums[i] = 2
        #     i += 1
        #     blueCount -= 1
        

        # Bubble Sort
        # for i in range(len(nums)):
        #     for j in range(len(nums) - 1):
        #         if nums[j] > nums[j + 1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+ 1] = temp
                