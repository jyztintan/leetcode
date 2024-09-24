class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            start = curr
            end = curr + 1
            interval = 0

            while start <= n:
                interval += min(n + 1, end) - start
                start *= 10
                end *= 10

            if interval <= k:
                k -= interval
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr


print(Solution().findKthNumber(10, 3))
