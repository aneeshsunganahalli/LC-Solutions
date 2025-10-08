import java.util.*;
// 2300
class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] pairs = new int[n];
        for (int i = 0; i < n; i++)
            pairs[i] = 0;
        
        Arrays.sort(potions);
        for (int s = 0; s < n; s++) {
            int lo = 0;
            int hi = m - 1;
            int val = -1;

            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                long product = (long)potions[mid] * (long)spells[s];
                if (product >= success) {
                    val = mid;
                    hi = mid - 1;
                }
                else
                    lo = mid + 1;
            }
            if (val != -1)
                pairs[s] = m - val;
            else
                pairs[s] = 0;
        }
        return pairs;
    }
}