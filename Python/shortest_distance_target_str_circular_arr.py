class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        best = inf
        for i, word in enumerate(words):
            if word == target:
                best = min(best, (startIndex - i) % n, (i - startIndex) % n)
        if best == inf:
            return -1
        return best
