class Solution:
    def maximumLength(self, s: str) -> int:
        # Keep a 2D array for char and length
        freq = [[0] * (len(s) + 1) for _ in range(26)]
        prev = s[0]
        streak = 1
        freq[ord(prev) - ord('a')][streak] = 1

        for idx in range(1, len(s)):
            curr = s[idx]
            if prev == curr:
                streak += 1
            else:
                prev = curr
                streak = 1
            freq[ord(curr) - ord('a')][streak] += 1

        best = -1
        for char_idx in range(26):
            for length in range(len(s) - 1, 0, -1):
                freq[char_idx][length] += freq[char_idx][length + 1]
                if freq[char_idx][length] >= 3:
                    ans = max(best, length)
                    break

        return best



from collections import Counter

# O(N^2) 2 pointer
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        left = 0
        d = Counter()
        best = -1

        while left < n:
            right = left
            while right < n and s[left] == s[right]:
                d[(s[left], right - left + 1)] += 1
                if d[(s[left], right - left + 1)] >= 3:
                    best = max(best, right - left + 1)
                right += 1
            left += 1

        return best

# Brute force : O(N^3)
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        def is_special(s):
            return len(set(s)) == 1

        def occurs_thrice(substring):
            m = len(substring)
            count = 0
            for left in range(n - m + 1):
                if s[left:left + m] == substring:
                    count += 1
            return count >= 3

        left = 0
        d = Counter()
        best = -1

        while left < n:
            right = left
            while right < n and is_special(s[left:right + 1]):
                d[s[left:right + 1]] += 1
                if d[s[left:right + 1]] >= 3:
                    best = max(best, right - left + 1)
                right += 1
            left += 1

        return best


assert Solution().maximumLength('aaaa') == 2