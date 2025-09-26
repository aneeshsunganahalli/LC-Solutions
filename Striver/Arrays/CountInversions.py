"""
Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].
"""

class Solution:
    def inversionCount(self, nums):
        n = len(nums)
        
        def mergeSort(nums, l, r):
            count = 0
            if l >= r:  return count
            
            mid = (l + r) // 2
            count +=  mergeSort(nums, l, mid)
            count += mergeSort(nums, mid +1 , r)
            count += merge(nums, l, mid, r)
            return count
            
        def merge(nums, low, mid, high):
            count = 0
            left = low
            right = mid + 1
            
            temp = []
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    count += mid - left + 1
                    right += 1
                    
            while (left <= mid):
                temp.append(nums[left])
                left += 1

            while (right <= high):
                temp.append(nums[right])
                right += 1
                
            for i in range(len(temp)):
                nums[low + i] = temp[i]
            return count
                
    
        
        return mergeSort(nums, 0, n - 1)
            
            
            
            
            
            
            