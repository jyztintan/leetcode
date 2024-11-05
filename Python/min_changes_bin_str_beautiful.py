class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0

        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                ans += 1

        return ans


class Solution:
    def minChanges(self, s: str) -> int:
        ptr, count = 1, 1
        ans = 0

        s = list(s)
        n = len(s)
        while ptr < n:
            while ptr < n and s[ptr] == s[ptr - 1]:
                count += 1
                ptr += 1
            if count % 2:
                ans += 1
                if s[ptr] == '0':
                    s[ptr] = '1'
                else:
                    s[ptr] = '0'
                ptr += 1

            ptr += 1
            count = 1


        return ans

# print(Solution().minChanges("11000111"))