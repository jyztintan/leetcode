class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left, right = 0, n - 1
        while colors[left] == colors[-1]:
            left += 1
        while colors[right] == colors[0]:
            right -= 1
        return max(n - 1 - left, right)
