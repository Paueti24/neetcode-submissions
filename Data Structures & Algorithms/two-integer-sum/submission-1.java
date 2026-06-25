class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            if (set.contains(target - n)) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[j] == target - n) {
                        int[] ans = new int[2];
                        ans[0] = i;
                        ans[1] = j;
                        return ans;
                    }
                }
            }
        }
        return null;
    }
}
