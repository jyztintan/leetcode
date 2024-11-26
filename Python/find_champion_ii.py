class Solution:
    def findChampion(self, n: int, edges) -> int:
        marked = [0] * n
        for u, v in edges:
            marked[v] = 1

        champion = -1
        for i, v in enumerate(n):
            if v == 0:
                if champion != -1:
                    return -1
                champion = i

        return champion

