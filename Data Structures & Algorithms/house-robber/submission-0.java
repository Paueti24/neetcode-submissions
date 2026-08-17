class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        
        int h0 = nums[0];
        int h1 = Math.max(nums[0], nums[1]);
        int h2 = h1;
        for (int j = 2; j < nums.length; j++) {
            h2 = Math.max(nums[j] + h0, h1);
            h0 = h1;
            h1 = h2;
        }
        return h2;
    }
}
