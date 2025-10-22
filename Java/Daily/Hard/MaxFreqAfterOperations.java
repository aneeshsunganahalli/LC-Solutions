import java.util.*;
// 3347
class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {

        Arrays.sort(nums);
        int res = 0;
        int l = 0, r = 0;
        Map<Integer, Integer> freq = new HashMap<>();

        for (int n: nums)
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        
        for (int n: nums) {
            while (nums[l] < n - k) 
                l += 1;
            while (r < nums.length && nums[r] <= n + k)
                r += 1;
            
            int window = r - l;
            int ops = window - freq.get(n);
            res = Math.max(res, freq.get(n) + Math.min(numOperations, ops));
        }

        // For numbers not in the array
        l = 0;
        for (int h = 0; h < nums.length; h++) {
            while(nums[l] < nums[h] - 2 * k)
                l += 1;
            res = Math.max(res, Math.min(h - l + 1, numOperations));
        }
        
        return res;

   }
}