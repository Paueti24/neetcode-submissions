class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            int area = (j - i);
            if (height[i] <= height[j]) {
                area *= height[i++];
            } else {
                area *= height[j--];
            }
            if (area > max) { max = area; }
        }
        return max;
    }
}