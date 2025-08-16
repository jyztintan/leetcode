class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i, c in enumerate(num):
            num[i] = '9'
            if c == '6':
                break
        return int("".join(num))
