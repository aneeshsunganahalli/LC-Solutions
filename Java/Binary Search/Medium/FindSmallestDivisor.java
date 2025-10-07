// 1283
class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int max = 0;
        for (int num : nums) {
            max = Math.max(max, num);
        }

        int low = 1, high = max;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (isValid(nums, mid, threshold)) {
                high = mid; // divisor works, try smaller
            } else {
                low = mid + 1; // divisor too small, increase
            }
        }
        return low;
    }

    private boolean isValid(int[] nums, int divisor, int threshold) {
        int sum = 0;
        for (int num : nums) {
            sum += (num + divisor - 1) / divisor; // ceil(num/divisor)
            if (sum > threshold) return false; // prune early
        }
        return true;
    }
}