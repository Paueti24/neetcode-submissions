class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>(nums.length);
        for (int n : nums) {
            if (set.contains(n)) { return true; }
            set.add(n);
        }
        return false;
    }
}