class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>((int)(nums.length / 0.75f) + 1);
        for (int n : nums) {
            if (set.contains(n)) { return true; }
            set.add(n);
        }
        return false;
    }
}