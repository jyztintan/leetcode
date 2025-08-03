# 2 pointer
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        pos = [p for p, _ in fruits]
        qty = [v for _, v in fruits]
        n = len(pos)

        # prefix sums over qty
        ps = [0]
        for v in qty:
            ps.append(ps[-1] + v)

        def window_sum(i, j):
            return ps[j + 1] - ps[i]

        def travel_cost(L, R, S):
            # min steps to cover [L, R] starting at S
            if R <= S:          # all on the left
                return S - L
            if L >= S:          # all on the right
                return R - S
            # both sides
            return (R - L) + min(S - L, R - S)

        ans = 0
        i = 0
        for j in range(n):
            # shrink from the left while too expensive
            while i <= j and travel_cost(pos[i], pos[j], startPos) > k:
                i += 1
            ans = max(ans, window_sum(i, j))
        return ans


# Simulate
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        positions = [p for p, _ in fruits]
        amounts = [v for _, v in fruits]
        prefix_sum = [0]
        for v in amounts:
            prefix_sum.append(prefix_sum[-1] + v)

        def window_sum(left, right):
            if left > right:
                return 0
            i = bisect_left(positions, left)
            j = bisect_right(positions, right) - 1
            if i > j:
                return 0
            return prefix_sum[j + 1] - prefix_sum[i]

        best = max(window_sum(startPos - k, startPos), window_sum(startPos, startPos + k))
        for pos, _ in fruits:
            if pos < startPos - k:
                continue
            elif pos > startPos + k:
                break

            spent = abs(startPos - pos)
            remain = k - 2 * spent
            if remain < 0:
                continue
            if pos < startPos:
                collected = window_sum(startPos - spent, startPos - 1) + window_sum(startPos, startPos + remain)
            else:
                collected = window_sum(startPos, startPos + spent) + window_sum(startPos - remain, startPos - 1)
            best = max(best, collected)
        return best
