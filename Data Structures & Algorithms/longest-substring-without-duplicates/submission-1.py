class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLen = 0
        i, j = 0,-1
        while j < len(s) - 1:
            j += 1
            if s[j] in chars:
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1
                # chars.remove(s[i])
                i += 1
            else:
                chars.add(s[j])
                maxLen = max(maxLen, j - i + 1)
        return maxLen