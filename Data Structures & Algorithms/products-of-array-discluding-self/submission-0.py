class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1 # except zeros
        zeros = 0 # counter of '0'
        for n in nums:
            if n == 0: # not multiply
                zeros += 1
                if zeros >= 2:
                    return [0] * len(nums)
            else:
                totalProd *= n # multiply
        
        # return (totalProd / n) if there are no zeros
        if zeros == 0:
            return [totalProd // i for i in nums]
        # when there's a zero, return all zeros except the '0' element
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = totalProd
                break
        return res
