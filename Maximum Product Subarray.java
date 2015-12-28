public class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length==0) return 0;
        int localSmall = nums[0];
        int localBig = nums[0];
        int res = nums[0];
        
        for (int i=1;i<nums.length;++i) {
            int elem = nums[i];
            int maxLocal = localBig;
            localBig = Math.max(Math.max(elem*localBig, elem), elem*localSmall);
            localSmall = Math.min(Math.min(elem*maxLocal, elem), elem*localSmall);
            res = Math.max(res, localBig);
        }
        
        return res;
        
    }
}
