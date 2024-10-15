class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        black = 0
        for ball in s:
            if ball == '1':
                black += 1
            else:
                count += black
        return count


print(Solution().minimumSteps('100'))

