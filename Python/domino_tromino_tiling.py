# Bottom up
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n <= 2:
            return n

        f = [0] * (n + 1)
        p = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        p[2] = 1
        for k in range(3, n + 1):
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD
            p[k] = (f[k - 2] + p[k - 1]) % MOD
        return f[n]

# Top down
class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        @cache
        def partial(n):
            if n == 2:
                return 1
            # 1) Add a L block to f(n - 2): ||||L
            # 2) Add a | block to the left of p(n - 1): |L
            return (full(n - 2) + partial(n - 1)) % MOD

        @cache
        def full(n):
            if n <= 2:
                return n
            # 1) Add a vertical domino on the right to f(n - 1)
            # 2) Add 2 vertical dominoes on the right to f(n - 2)
            # 3) 2 ways to add a tromino to p(n - 1): LꞀ and Г⅃
            return (full(n - 1) + full(n - 2) + partial(n - 1) * 2) % MOD

        return full(n)
