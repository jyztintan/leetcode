class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Simplified equation putting it together
        return (n * m) // 2

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # n is odd, m is even
        total = (n + 1) // 2 * (m // 2)
        # m is odd, n is even
        total += (m + 1) // 2 * (n // 2)
        return total
