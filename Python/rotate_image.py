class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose in a diagonal fashion
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reflect, in a row by row fashion
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][- col - 1] = matrix[row][- col - 1], matrix[row][col]
