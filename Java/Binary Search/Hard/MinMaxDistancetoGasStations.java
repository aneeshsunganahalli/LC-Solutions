/*
We have a horizontal number line. On that number line, we have gas stations at positions stations[0], stations[1], ..., stations[n-1]. Now, we add k more gas stations so that d, the maximum distance between adjacent gas stations, is minimized. We have to find the smallest possible value of d. Find the answer exactly to 2 decimal places.
Note: stations is in a strictly increasing order.

Examples:

Input: stations[] = [1, 2, 3, 4, 5], k = 2
Output: 1.00
Explanation: Since all gaps are already equal (1 unit each), adding extra stations in between does not reduce the maximum distance.
 */
class Solution {
    public double minMaxDist(int[] stations, int k) {
        
        int n = stations.length;
        double lo = 0;
        double hi = 0;
        
        for(int i = 0; i < n - 1; i++){
            hi = Math.max(hi, stations[i + 1] - stations[i]);
        }
        
        double diff = Math.pow(10, -3);
        while (hi - lo > diff) {
            double mid = (hi + lo) / 2.0;
            int count = gasStationsRequired(mid, stations);
            // We check how many stations needed such that distance between any two is atmost mid
            if (count > k)
                lo = mid;
            else
                hi = mid;
        }
        return hi;
        
    }
    
    public int gasStationsRequired(double distance, int[] arr) {
        int n = arr.length;
        int count = 0;
        
        for (int i = 1; i < n; i++) {
            double gap = (arr[i] - arr[i - 1]);
            int numbersInBetween = (int)(Math.ceil( gap / distance) - 1);
            // Checking for cases where gap is perfectly divisble, when it is, we need one less than actual quotient
            // gap = 4, distance = 2, gap/dist = 2 but only one station needed to achieve this
            if (gap == distance * numbersInBetween)
                numbersInBetween -= 1;
            count += numbersInBetween;
        }
        return count;
    }
}
