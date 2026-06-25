class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>((int)(nums.length / 0.75f) + 1);
        for (int n : nums) {
            if (!set.add(n)) { return true; }
        }
        return false;
        
        /*Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) { return true; }
        }
        return false;*/
    }
}