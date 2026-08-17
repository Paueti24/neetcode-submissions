from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def money(i):
            if i >= len(nums):
                return 0

            return max(nums[i] + money(i+2), money(i+1))
            
        return money(0)
