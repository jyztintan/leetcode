class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        best = float('inf')
        for target in freq.values():
            deletions = 0
            for count in freq.values():
                if count < target:
                    deletions += count
                else:
                    deletions += max(0, count - target - k)
            best = min(best, deletions)
        return best
