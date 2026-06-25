class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character, Integer> chars = new HashMap<>();
        for (char c : text.toCharArray()) {
            chars.put(c, chars.getOrDefault(c, 0) + 1);
        }
        int minTimes = 100000;
        for (char c : "ban".toCharArray()) {
            int times = chars.getOrDefault(c, 0);
            if (times < minTimes) { minTimes = times; }
        }
        for (char c : "lo".toCharArray()) {
            int times = chars.getOrDefault(c, 0) / 2;
            if (times < minTimes) { minTimes = times; }
        }
        return minTimes;
    }
}