class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        memoize = {}
        n, m = len(s), len(p)
        def dp(i, j):
            if (i, j) in memoize:
                return memoize[(i, j)]

            # if pattern is empty, return True iff s is also empty
            if j == m:
                memoize[(i, j)] = i == n
                return i == n

            # If s is empty or the first char of s and p do not match
            if i == n or (p[j] != s[i] and p[j] != '.'):
                # Check if the next char in pattern is * in which we skip over this optional
                if j + 1 < m and p[j + 1] == '*':
                    memoize[(i, j)] = dp(i, j + 2)
                else:
                    memoize[(i, j)] = False
                return memoize[(i, j)]

            if j + 1 < m and p[j + 1] == '*':
                # Either we skip over or we just continue iterating seems its a wildcard
                memoize[(i, j)] = dp(i, j + 2) or dp(i + 1, j)
            else:
                memoize[(i, j)] = dp(i + 1, j + 1)
            return memoize[(i, j)]

        return dp(0, 0)


print(Solution().isMatch('aa', 'a*'))
