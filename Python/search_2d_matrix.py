class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Target is out of range in the matrix
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        low, high = 0, m - 1
        while low <= high:
            row = (low + high) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif matrix[row][0] > target:
                high = row - 1
            else:
                low = row + 1

        left, right = 0, n - 1
        row = matrix[row]
        while left <= right:
            mid = (left + right) // 2
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# print(Solution().searchMatrix(matrix, target))