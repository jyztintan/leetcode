class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        freq = {'a': 0, 'b': 0, 'c': 0}
        for c in s:
            freq[c] += 1

        for c in freq:
            if freq[c] < k:
                return -1

        left = 0
        n = len(s)
        window = {'a': 0, 'b': 0, 'c': 0}
        best = float('inf')

        for right in range(n):
            window[s[right]] += 1

            while left <= right and (freq['a'] - window['a'] < k or freq['b'] - window['b'] < k or freq['c'] - window['c'] < k):
                window[s[left]] -= 1
                left += 1

            best = min(best, n - (right - left + 1))

        return best


print(Solution().takeCharacters('aabaaaacaabc', 2))