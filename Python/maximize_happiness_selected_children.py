class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        for count in range(k):
            total += max(0, happiness[count] - count)
        return total
