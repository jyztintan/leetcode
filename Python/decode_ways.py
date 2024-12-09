# Bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1

        ways = [0] * n
        ways[0] = 1
        if s[1] != '0':
            ways[1] = 1
        if 1 <= int(s[:2]) <= 26:
            ways[1] += 1

        for i in range(2, n):
            if s[i] != '0':
                ways[i] += ways[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                ways[i] += ways[i - 2]
        return ways[n - 1]


class Solution:
    def numDecodings(self, s: str) -> int:
        memoize = {len(s) : 1}

        def check(ptr):
            if ptr in memoize:
                return memoize[ptr]
            if s[ptr] == "0":
                memoize[ptr] = 0
                return memoize[ptr]

            total = check(ptr + 1)
            if (ptr + 2) <= len(s) and int(s[ptr:ptr+2]) <= 26:
                total += check(ptr + 2)
            memoize[ptr] = total
            return total

        check(0)
        return memoize[len(s)]