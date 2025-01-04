# Time: O(N), two passes - one for getting initial, then second for iterating through possible 'splits'
# Spcae: O(1)
class Solution:
    def maxScore(self, s: str) -> int:




# Time: O(N), two passes - one for getting initial, then second for iterating through possible 'splits'
# Spcae: O(1)
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        for i in range(n):
            if i == 0:
                if s[i] == '0':
                    left += 1
            elif s[i] == '1':
                right += 1

        best = left + right
        for i in range(1, n - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            best = max(best, left + right)

        return best
