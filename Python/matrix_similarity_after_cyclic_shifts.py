class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for row in range(m):
            delta = k if row % 2 == 0 else -k
            for col in range(n):
                if mat[row][col] != mat[row][(col + delta) % n]:
                    return False
        return True
