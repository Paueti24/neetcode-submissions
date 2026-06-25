class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        int[] memo = new int[n+1];
        
        for (int i = 1; i <= n; i++) {
            res[i] = countBitsOnce(i, memo);
        }
        return res;
    }

    private int countBitsOnce(int n, int[] memo) {
        if (n == 0) return 0;
        if (memo[n] != 0) return memo[n];

        int res = n % 2 + countBitsOnce(n / 2, memo);
        memo[n] = res;
        return res;
    }

}
