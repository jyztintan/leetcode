from functools import lru_cache

class Solution:
    def maxA(self, n: int) -> int:
        @lru_cache(None)
        def dp(moves):
            if moves <= 0:
                return 0

            # Type 'A'
            best = dp(moves - 1) + 1

            # Ctrl-A, Ctrl-C, then Ctrl-Vs
            # reserve 2 moves for select-all and copy, then remaining moves for pastes
            for prev in range(moves - 2):
                pastes = moves - prev - 1
                best = max(best, dp(prev) * pastes)
            return best

        return dp(n)
