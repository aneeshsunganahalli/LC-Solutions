class Solution {
// 1011
    public boolean possible(int[] weights, int days, int capacity) {
            int total = 0;
            int daysTaken = 1;
            for (int w: weights) {
                if (total + w > capacity) {
                    daysTaken += 1;
                    if ( w> capacity)
                        return false;
                    total = w;
                }
                else
                    total += w;
            }
            
            if (daysTaken <= days)
                return true;
            return false;
        }

    public int shipWithinDays(int[] weights, int days) {
        int lo = weights[0];
        int hi = 0;
        for (int w: weights) {
            if (w > lo)
                lo = w;
            hi += w;
        }
        int res = hi;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            if (possible(weights, days, mid)) {
                res = mid;
                hi = mid - 1;
            }
            else
                lo = mid + 1;
        }
        return res;
    }
}