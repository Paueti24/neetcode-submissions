class Solution {
    public int findMin(int[] nums) {
        return findMin(nums, 0, nums.length - 1);
    }

    private int findMin(int[] nums, int ini, int fi) {
        if (nums[ini] <= nums[fi]) return nums[ini];

        int m = (ini + fi) / 2;
        if (nums[ini] <= nums[m]) {
            return findMin(nums, m+1, fi);
        } else { // nums[ini] > nums[m]
            return findMin(nums, ini, m);
        }

    }
}
