class Solution:
    def concatenatedBinary(self, n: int) -> int:
        string = []
        for num in range(n + 1):
            string.extend(bin(num)[2:])
        return int("".join(string), 2) % (10 ** 9 + 7)
