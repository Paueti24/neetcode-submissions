class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def binSearch(i, j):
            if (i > j):
                return -1

            m = (i + j) // 2
            
            if target < nums[m]:
                return binSearch(i, m-1)
            elif target > nums[m]:
                return binSearch(m+1, j)
            else:
                return m
        
        return binSearch(0, n-1)
            