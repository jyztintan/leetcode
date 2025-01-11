class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final = 0
        for direction, amount in shift:
            if direction:
                final += amount
            else:
                final -= amount

        final = final % len(s)
        return s[-final:] + s[:-final]
