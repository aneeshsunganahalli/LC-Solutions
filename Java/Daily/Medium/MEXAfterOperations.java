import java.util.*;
// 2598
class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        
        Map<Integer, Integer> freq = new HashMap<>();
        for ( int i = 0; i < nums.length; i++) {
            int rem = ((nums[i] % value) + value) % value;
            freq.put(rem, freq.getOrDefault(rem, 0) + 1);
        }
        int i = 0;
        while (true) {
            int rem = i % value;
            int count = freq.getOrDefault(rem, 0);
            if (count == 0)
                return i;
            freq.put(rem, count - 1);
            i++;
        }
    }
}