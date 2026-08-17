from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def money(i):
            if i == len(nums) - 1:
                return nums[i]
            if i == len(nums) - 2:
                return max(nums[i], nums[i+1])
            
            return max(nums[i] + money(i+2), money(i+1))
        return money(0)
