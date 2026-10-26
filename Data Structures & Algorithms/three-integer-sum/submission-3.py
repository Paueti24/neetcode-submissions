class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            elif nums[i] > 0:
                break
            
            j, k = i+1, n-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else: # sum == 0
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1

        return triplets