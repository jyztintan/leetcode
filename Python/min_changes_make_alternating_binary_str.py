class Solution:
    def minOperations(self, s: str) -> int:
        start_zero = 0
        start_one = 0
        zero = False
        for c in s:
            if ((c == "0") != zero):
                start_zero += 1
            if (c == "0") == zero:
                start_one += 1
            zero = not zero

        return min(start_zero, start_one)

