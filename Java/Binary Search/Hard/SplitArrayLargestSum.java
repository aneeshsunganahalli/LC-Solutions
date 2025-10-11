// 410
class Solution {
    public int splitArray(int[] nums, int k) {
        int lo = nums[0];
        int hi = nums[0];
        for (int num : nums) {
            if (num > lo) {
                lo = num;
            }
            hi += num;
        }

        int res = hi;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            if (possible(nums, k, mid)) {
                res = mid;
                hi = mid - 1;
            } else
                lo = mid + 1;
        }
        return res;
    }

    public boolean possible(int[] nums, int k, int mid) {
        int total = 0;
        int sub = 1;
        for(int i = 0; i < nums.length; i++) {
            if (total + nums[i] > mid) {
                sub += 1;
                total = nums[i];
                if (sub > k)
                    return false;
            }
            else
                total += nums[i];
        }
        return true;
    }
}