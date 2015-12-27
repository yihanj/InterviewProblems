public List<List<Integer>> threeSum(int[] nums) {
    
    List<List<Integer>> res = new ArrayList<>();
    
    if(nums == null || nums.length < 3) {
        return res;
    }
    Arrays.sort(nums);
    
    for(int i = 0; i < nums.length; i++) {
        if(i > 0 && nums[i] == nums[i - 1]) continue;        
        int target = 0 - nums[i];
        int j = i + 1, k = len - 1;
        while(j < k) {
            if(nums[j] + nums[k] == target) {
                res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                while(j < k && nums[j] == nums[j + 1]) j++;  
                while(j < k && nums[k] == nums[k - 1]) k--;  
                j++; k--;
            } else if(nums[j] + nums[k] < target) {
                j++;
            } else {
                k--;
            }
        }
    }
    return res;
}
