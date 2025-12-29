class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        curr = 0
        for right in range(k):
            curr += calories[right]

        points = 0
        n = len(calories)
        for right in range(k, n):
            points += -1 if curr < lower else (1 if curr > upper else 0)
            curr -= calories[right - k]
            curr += calories[right]
        points += -1 if curr < lower else (1 if curr > upper else 0)
        return points
