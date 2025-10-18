import java.util.*;
// 3397
class Solution {
    public int maxDistinctElements(int[] nums, int k) {

        int last_picked = Integer.MIN_VALUE;
        Arrays.sort(nums);
        int distinct = 0;
        for (int num: nums) {
            int low = num - k;
            int high = num + k;

            if (last_picked < low)
                last_picked = low;
            else
                last_picked += 1;
            
            if (last_picked <= high)
                distinct++;
            else
                last_picked -= 1;
        }

        return distinct;
    }
}