class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        letters, remaining, window = {}, {}, {}
        for ch in t:
            letters[ch] = letters.get(ch, 0) + 1
            remaining[ch] = remaining.get(ch, 0) + 1
        minStr = ""
        l, r = 0,-1
        while l < n:
            # slide right until 
            while(remaining and r+1 < n):
                r += 1
                ch = s[r]
                window[ch] = window.get(ch, 0) + 1 
                if ch in remaining:
                    remaining[ch] -= 1
                    if remaining[ch] == 0:
                        remaining.pop(ch)
            # minimize size
            if not remaining and ((r - l + 1) < len(minStr) or minStr == ""):
                minStr = s[l:r+1]
            # slide 1 letter left
            ch = s[l]
            if ch in letters and window[ch] <= letters[ch]:
                remaining[ch] = remaining.get(ch, 0) + 1
            window[ch] -= 1
            l += 1
        return minStr
        
            
            
             
