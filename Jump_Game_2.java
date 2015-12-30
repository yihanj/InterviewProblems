public class Solution {
    public int jump(int[] nums) {
        /* greedy BFS algorithm
        divide array by level, then # of level reveals the result.
        */
        if (nums.length < 2) return 0;
        int level = 0, curMax = 0, i=0, nextMax = 0;
        
        while (curMax - i + 1 >0){  // for each level
            level++;
            for ( ; i<=curMax; ++i) { //update max 
                nextMax = Math.max(nextMax, nums[i] + i);
                if (nextMax >=nums.length -1 ) return level;
            }
            curMax = nextMax;
        }
        return 0;
    }
}
