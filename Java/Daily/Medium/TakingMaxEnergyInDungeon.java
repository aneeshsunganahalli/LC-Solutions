// 3147
class Solution {
    public int maximumEnergy(int[] energy, int k) {

        int n = energy.length;
        int[] prefix = new int[n];

        for (int i = 0; i < n; i++)
            prefix[i] = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            if (i + k >= n)
                prefix[i] = energy[i];
            else
                prefix[i] = energy[i] + prefix[i + k];
        }

        int maxVal = prefix[0];
        for (int num : prefix) {
            if (num > maxVal)
                maxVal = num;
        }
        return maxVal;
    }
}