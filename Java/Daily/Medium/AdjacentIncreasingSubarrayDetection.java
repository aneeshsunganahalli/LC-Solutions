import java.util.*;
// 3350
class Solution {
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int prev = 0;
        int res = 0;
        int i = 0;
        int N = nums.size();
        while (i < N) {
            int curr = check(nums, i);
            res = Math.max(res, Math.min(prev, curr));
            res = Math.max(res, curr / 2);
            prev = curr;
            i += curr;
        }
        return res;
    }

    public int check(List<Integer> nums, int i) {
        int count = 1;
        int N = nums.size();
        while (i + 1 < N && nums.get(i) < nums.get(i + 1)) {
            i += 1;
            count += 1;
        }
        return count;
    }
}