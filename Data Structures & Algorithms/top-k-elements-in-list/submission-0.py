class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n in map:
            freq[map[n]].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                res += freq[i]
                k -= len(freq[i])
                if k == 0:
                    break
        return res
