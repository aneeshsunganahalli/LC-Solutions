import java.util.*;
// 1488
class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        Map<Integer, Integer> full = new HashMap<>();
        TreeSet<Integer> dryDays = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            int lake = rains[i];

            if (lake == 0) {
                dryDays.add(i);
                res[i] = 1; // placeholder
            } else {
                if (full.containsKey(lake)) {
                    int lastFilled = full.get(lake);
                    Integer dryDay = dryDays.ceiling(lastFilled + 1);
                    if (dryDay == null) return new int[0]; // no valid dry day
                    res[dryDay] = lake;
                    dryDays.remove(dryDay);
                }
                full.put(lake, i);
                res[i] = -1;
            }
        }

        return res;
    }
}
