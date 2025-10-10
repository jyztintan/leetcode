class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        wizards = [0] * n

        for potion in mana:
            time = 0
            # take the earliest time for each wizard and make the potion
            for idx in range(n):
                time = max(time, wizards[idx]) + skill[idx] * potion
            wizards[n - 1] = time
            # Retroactively take the latest timing so that potion is processed continuously
            for idx in range(n - 2, -1, -1):
                wizards[idx] = wizards[idx + 1] - skill[idx + 1] * potion
        return wizards[n - 1]
