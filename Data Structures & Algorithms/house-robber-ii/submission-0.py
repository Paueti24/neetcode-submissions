class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            rob0, rob1 = 0,0
            for n in nums:
                temp = max(n + rob0, rob1)
                rob0 = rob1
                rob1 = temp
            return rob1
        robbing0 = nums[0] + houseRobber(nums[2:-1])
        notRobbing0 = houseRobber(nums[1:])
        return max(robbing0, notRobbing0)