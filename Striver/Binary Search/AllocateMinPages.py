"""
Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

    Each student receives atleast one book.
    Each student is assigned a contiguous sequence of books.
    No book is assigned to more than one student.

The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: If it is not possible to allocate books to all students, return -1.

Examples:
Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
=> [12] and [34, 67, 90] Maximum Pages = 191
=> [12, 34] and [67, 90] Maximum Pages = 157
=> [12, 34, 67] and [90] Maximum Pages = 113.
The third combination has the minimum pages assigned to a student which is 113.
"""
class Solution:
    def findPages(self, arr, k):
        
        if len(arr) < k:
            return -1
        # Defining a function possible(mid) that checks if it’s possible to allocate books so that no student gets more than mid pages.
        def possible(mid):
            students = 1
            pages = 0
            for book in arr:
                if pages + book > mid:
                    pages = book
                    students += 1
                    if students > k:
                        return False
                else:
                    pages += book
                    
            return True
        
        lo = max(arr)
        hi = sum(arr)
        res= hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res