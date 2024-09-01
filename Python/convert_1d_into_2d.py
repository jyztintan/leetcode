from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ptr = 0
        mat = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                mat[row][col] = original[ptr]
                ptr += 1
        return mat
