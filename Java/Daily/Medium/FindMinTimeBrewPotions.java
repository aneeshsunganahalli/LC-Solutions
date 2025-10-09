// 3494
class Solution {
    public long minTime(int[] skill, int[] mana) {
        int n = skill.length;   // number of wizards
        int m = mana.length;    // number of potions

        // Compute prefix sum of wizard skills
        long[] prefixSkill = new long[n];
        for (int i = 1; i < n; i++) {
            prefixSkill[i] = prefixSkill[i - 1] + skill[i];
        }

        // Time for the first potion at the first wizard
        long potionStartTime = (long) skill[0] * mana[0];

        // Loop over remaining potions
        for (int j = 1; j < m; j++) {
            long maxDiff = (long) skill[0] * mana[j]; // includes first wizard

            // Check bottleneck for wizards 1 to n-1
            for (int i = 1; i < n; i++) {
                long currDiff = (long) mana[j - 1] * prefixSkill[i] - (long) mana[j] * prefixSkill[i - 1];
                if (currDiff > maxDiff) {
                    maxDiff = currDiff;
                }
            }

            // Add bottleneck delay for this potion
            potionStartTime += maxDiff;
        }

        // Add time for last potion to pass through all wizards
        long totalTime = potionStartTime + (long) mana[m - 1] * prefixSkill[n - 1];
        return totalTime;
    }
}
