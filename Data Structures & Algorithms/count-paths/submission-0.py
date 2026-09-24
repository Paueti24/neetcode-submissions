from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def paths(i,j):
            if i == m - 1:
                return 1
            elif j == n - 1:
                return 1
            
            return paths(i+1, j) + paths(i, j+1)
        
        return paths(0,0)