class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '@'
            res += s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            n = ""
            while s[i].isdigit():
                n += s[i]
                i += 1
            n = int(n)
            # s[i] = '@'
            i += 1
            thisStr = ""
            for _ in range(n):
                thisStr += s[i]
                i += 1
            res.append(thisStr)
        return res


