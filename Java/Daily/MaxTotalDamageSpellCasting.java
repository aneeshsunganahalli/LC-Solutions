import java.util.*;
// 3186
class Solution {
    public long maximumTotalDamage(int[] power) {

        Map<Integer, Integer> freq = new HashMap<>();
        for(int p: power)
            freq.put(p, freq.getOrDefault(p,0) + 1);

        ArrayList<Integer> sorted_keys = new ArrayList<>(freq.keySet());
        Collections.sort(sorted_keys);
        int n = sorted_keys.size();

        long[] dp = new long[n];

        for (int i = 0; i < n; i++) {
            int currPower = sorted_keys.get(i);
            long damage = (long)currPower * freq.get(currPower);

            int index = i - 1;
            while ( index >= 0 && sorted_keys.get(index) >= currPower - 2)
                index--;

            long skip = i > 0 ? dp[i - 1]: 0;
            long pick = damage + (index >= 0 ? dp[index] : 0);
            
            dp[i] = Math.max(skip, pick);
        }
        return dp[n - 1];
    }
}