class Solution {
    public int maxProfit(int[] prices) {
        int lower = prices[0], maxProfit = 0;
        for (int p : prices) {
            if (p <= lower) { lower = p; }
            else if (p - lower > maxProfit) { maxProfit = p - lower; }
        }
        return maxProfit;
    }
}
