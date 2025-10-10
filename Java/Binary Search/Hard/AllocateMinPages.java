/*
 * Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

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
 */


class Solution {
    public int findPages(int[] arr, int k) {
        
        if (arr.length < k)
            return -1;
        
        int lo = arr[0];
        int hi = arr[0];
        
        for (int num: arr) {
            if (num > lo)
                lo = num;
            hi += num;
        }
        
        int res = hi;
        
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (possible(arr, k, mid)) {
                res = mid;
                hi = mid - 1;
            }
            else
                lo = mid + 1;
        }
        
        return res;
        
    }
    
    public boolean possible(int[]arr, int k, int mid) {
        int students = 1;
        int pages = 0;
        
        for (int book: arr) {
            if (pages + book > mid) {
                students += 1;
                pages = book;
                if (students > k)
                    return false;
            } 
            else
                pages += book;
        }
        return true;
    }
}