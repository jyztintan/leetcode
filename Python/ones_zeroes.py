class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num_count = []
        for num in strs:
            num_count.append((num.count('0'), num.count('1'), num))

        length = len(strs)

        dp = {}

        def backtrack(ptr, m, n):
            if (ptr, m, n) in dp:
                return dp[(ptr, m, n)]
            if ptr == length:
                return 0
            num_zero, num_one, num = num_count[ptr]
            ans = backtrack(ptr + 1, m, n)
            if num_zero <= m and num_one <= n:
                ans = max(ans, 1 + backtrack(ptr + 1, m - num_zero, n - num_one))
            dp[(ptr, m, n)] = ans
            return ans

        return backtrack(0, m, n)

