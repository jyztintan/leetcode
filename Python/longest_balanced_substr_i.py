# Time Complexity = O(c * N ^ 2) where c is the number of unique characters, bounded by 26 which is constant,
# hence surmised to say => O(N ^ 2)
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        best = 0
        for start in range(n):
            freq = defaultdict(int)
            for end in range(start, n):
                freq[s[end]] += 1
                if len(set(freq.values())) == 1:
                    best = max(best, end - start + 1)
        return best
