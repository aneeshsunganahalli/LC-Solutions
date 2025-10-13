/*
Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

Input: a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
Output: 10
Explanation: Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.
 */
class Solution {
    public int kthElement(int[] a, int[] b, int k) {
        // Ensure a is the smaller array
        if (a.length > b.length) {
            return kthElement(b, a, k);
        }

        int lo = 0; // smallest possible elements to take from a
        int hi = a.length;    // largest possible elements to take from a

        while (lo <= hi) {
            int mid = (lo + hi) / 2;  // elements taken from a
            int j = k - mid;          // elements taken from b

            int Aleft  = mid > 0 ? a[mid - 1] : Integer.MIN_VALUE;
            int Aright = mid < a.length ? a[mid] : Integer.MAX_VALUE;
            int Bleft  = j > 0 ? b[j - 1] : Integer.MIN_VALUE;
            int Bright = j < b.length ? b[j] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright) {
                return Math.max(Aleft, Bleft);
            } else if (Aleft > Bright) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
      return -1;
    }
}
