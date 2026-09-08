class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxSeq = 0
        for n in nums:
            if not (n - 1) in setNums:
                i = 0
                while n in setNums:
                    i += 1
                    n += 1
                maxSeq = max(maxSeq, i)
        return maxSeq
