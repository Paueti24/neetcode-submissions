class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) { return false; }
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int n = map.getOrDefault(c,0);
            map.put(c,n+1);
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            Integer n = map.get(c);
            if (n == null || n <= 0) { return false; }
            map.put(c,n-1);
        }
        return true;
    }
}
