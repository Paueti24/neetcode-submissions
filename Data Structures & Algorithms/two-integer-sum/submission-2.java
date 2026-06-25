class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = map.get(target - nums[i]);
            if (j != null) {
                int[] ans = new int[2];
                ans[0] = j; ans[1] = i;
                return ans;
            }
            map.put(nums[i],i);
        }
        return null;
    }
}
