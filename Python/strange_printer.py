class Solution:
    def strangePrinter(self, s: str) -> int:

        new_s = ""
        prev = ""
        for c in s:
            if c == prev:
                continue
            new_s += c
            prev = c

        s, n = new_s, len(new_s)

        memo = {}

        def min_prints(start, end):
            if start > end or end >= n:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            if end == start:
                return 1

            ans = min_prints(start + 1, end) + 1
            for ptr in range(start + 1, end + 1):
                if s[start] == s[ptr]:
                    ans = min(ans, min_prints(start, ptr - 1) + min_prints(ptr + 1, end))

            memo[(start, end)] = ans
            return ans

        return min_prints(0, n - 1)

print(Solution().strangePrinter("aa"))
print(Solution().strangePrinter("aabb"))

