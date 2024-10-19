class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        length = 2 ** n

        # First half
        if k < length//2:
            return self.findKthBit(n - 1, k)

        # Middle
        elif k == length//2:
            return '1'

        # Second half
        else:
            return '0' if self.findKthBit(n - 1, length - k) == '1' else '1'