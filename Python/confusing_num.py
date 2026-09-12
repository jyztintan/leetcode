class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {'0': 0, '1': 1, '6': 9, '8': 8, '9': 6}
        num = str(n)
        new = 0
        for i in range(len(num) - 1, -1, -1):
            c = num[i]
            if c not in rotate:
                return False
            new *= 10
            new += rotate[c]
        return new != n

