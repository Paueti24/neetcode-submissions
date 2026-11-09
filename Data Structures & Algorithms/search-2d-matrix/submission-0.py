class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, n*m-1
        while i <= j:
            mid = (i + j) // 2
            midElement = matrix[mid // m][mid % m]
            if midElement == target:
                return True
            elif target < midElement:
                j = mid - 1
            else:
                i = mid + 1
        return False
