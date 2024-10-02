from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        ranks = {}

        rank = 1
        prev = -1
        for num in sorted_arr:
            if prev == num:
                continue
            ranks[num] = rank
            prev = num
            rank += 1

        ans = [ranks[val] for val in arr]
        return ans