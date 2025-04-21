class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        lowest, highest = 0, 0
        curr = 0
        for diff in differences:
            curr += diff
            lowest = min(lowest, curr)
            highest = max(highest, curr)

        return max(0, upper - lower - highest + lowest + 1)
