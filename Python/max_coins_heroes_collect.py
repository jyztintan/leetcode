from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        m, n = len(heroes), len(monsters)
        hero_idxs = sorted(range(m), key=heroes.__getitem__)
        mons_idxs = sorted(range(n), key=monsters.__getitem__)
        output = [0] * m
        pick = j = 0
        for hero_idx in hero_idxs:
            while j < n and monsters[mons_idxs[j]] <= heroes[hero_idx]:
                pick += coins[mons_idxs[j]]
                j += 1
            output[hero_idx] = pick
        return output