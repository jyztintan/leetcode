class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        done = {}
        def count_subsequences(s_ptr, t_ptr):
            if (s_ptr, t_ptr) in done:
                return done[(s_ptr, t_ptr)]
            if s_ptr < t_ptr:
                return 0

            if t_ptr < 0:
                return 1

            ans = count_subsequences(s_ptr - 1, t_ptr)
            if s[s_ptr] == t[t_ptr]:
                ans += count_subsequences(s_ptr - 1, t_ptr - 1)

            done[(s_ptr, t_ptr)] = ans
            return ans


        return count_subsequences(n - 1, m - 1)

s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
