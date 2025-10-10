// 1539
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int lo = 0;
        int hi = arr.length;

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] - mid - 1 < k)
                lo = mid + 1;
            else
                hi = mid;
        }
        return hi + k;
    }
}