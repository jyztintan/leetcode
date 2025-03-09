class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k - 1])
        n = len(colors)
        count = 0
        left, right = 0, 1

        while right < n:
            while right < n and colors[right] != colors[right - 1]:
                right += 1

            if right - left >= k:
                count += right - left - k + 1
                left += 1
            left = right
            right += 1

        return count
