from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        correct_total = mean * (n + len(rolls))
        diff = correct_total - total
        if diff > n * 6 or diff < n:
            return []
        ans = []
        diff -= n
        for i in range(n):
            if not diff:
                ans.append(1)
            elif diff >= 5:
                ans.append(6)
                diff -= 5
            else:
                ans.append(1 + diff)
                diff = 0
        return ans



