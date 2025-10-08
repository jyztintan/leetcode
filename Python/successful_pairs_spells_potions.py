class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        ans = [0] * n
        sorted_spells = sorted((spell, i) for i, spell in enumerate(spells))
        sorted_potions = sorted(potions)

        def bin_search(curr_spell, high):
            low = 0
            while low < high:
                mid = (low + high) // 2
                if curr_spell * sorted_potions[mid] < success:
                    low = mid + 1
                else:
                    high = mid
            return low

        potion_ptr = m
        for spell, i in sorted_spells:
            potion_ptr = bin_search(spell, potion_ptr)
            ans[i] += m - potion_ptr
        return ans
