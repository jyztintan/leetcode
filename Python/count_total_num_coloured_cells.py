# O(1) Closed form solution
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1

# O(N) iterative solution
class Solution:
    def coloredCells(self, n: int) -> int:
        curr = 1
        for level in range(n):
            curr += level * 4
        return curr
