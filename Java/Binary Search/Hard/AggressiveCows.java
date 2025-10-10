/*
You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible. 
 */
import java.util.Arrays;
 class Solution {
    public int aggressiveCows(int[] stalls, int k) {
        
        Arrays.sort(stalls);
        int lo = 1;
        int max = stalls[0];
        int min = stalls[0];
        
        for (int num: stalls) {
            
            if (num > max)
                max = num;
                
            if (num < min)
                min = num;
        }
        
        int hi = max - min;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (possible(stalls,k,mid))
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return hi;
    }
    
    public boolean possible(int[] stalls, int k, int distance) {
        int cowCount = 1;
        int last = stalls[0];
        
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - last >= distance) {
                last = stalls[i];
                cowCount++;
            }
        }
        
        if (cowCount >= k)
            return  true;
        return false;
    }
}