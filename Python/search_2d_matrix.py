class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            row = (up + down) // 2
            if matrix[row][-1] >= target >= matrix[row][0]:
                break
            elif matrix[row][0] > target:
                down = row - 1
            else:
                up = row + 1

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            check = matrix[row][mid]
            if check == target:
                return True
            elif check < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
