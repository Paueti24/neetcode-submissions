class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        duplicates = set()
        map = {}
        for i in range(n):
            map[nums[i]] = map.get(nums[i], 0) + 1

        for i in range(n):
            map[nums[i]] -= 1
            for j in range(i,n-1):
                if j == i:
                    continue
                target = -nums[i] - nums[j]
                map[nums[j]] -= 1
                triplet_id = (min(nums[i], nums[j], target), max(nums[i], nums[j], target))
                if target in map and map[target] > 0 and triplet_id not in duplicates:
                    triplets.append([nums[i], nums[j], target])
                    duplicates.add(triplet_id)
                map[nums[j]] += 1
            map[nums[i]] += 1
                
        
        return triplets