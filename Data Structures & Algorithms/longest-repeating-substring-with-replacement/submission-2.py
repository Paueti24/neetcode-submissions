class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        letters = set()
        for l in s:
            letters.add(l)
        
        totalMax = 1
        for letter in letters:
            # sliding window
            thisMax = 1
            left = 0
            thisK = k
            for right in range(n):
                if s[right] != letter:
                    thisK -= 1
                    while thisK < 0:
                        if s[left] != letter:
                            thisK += 1
                        left += 1
                thisMax = max(thisMax, right - left + 1)
            totalMax = max(totalMax, thisMax)
            if totalMax == n:
                break
        return totalMax