from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        m,n = len(nums1),len(nums2)
        res = []

        while i < m and j < n:
            if nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]: 
                res.append(nums2[j])
                j += 1
            else:
                res.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i += 1
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1

        return res