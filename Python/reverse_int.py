class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        string_num = str(abs(x))
        num = int(string_num[::-1]) * sign
        if num > 2 ** 31 -1 or num < - 2 ** 31:
            return 0
        return num
    