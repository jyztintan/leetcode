class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        # The first 3 bulbs uniquely define the entire sequence
        n = min(3, n)

        # No presses allowed so only one state
        if presses == 0:
            return 1

        # 1 press allowed, possibly 2, 3 or 4 states depending on n
        if presses == 1:
            return [2, 3, 4][n - 1]
        # 2 presses allowed, possibly 2, 4 or 7 states depending on n
        elif presses == 2:
            return [2, 4, 7][n - 1]
        # More than 2 presses allowed, possibly 2, 4 or 8 states depending on n
        return [2, 4, 8][n - 1]