class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        curr = 0
        best = 0
        for right in range(k):
            if blocks[right] == "W":
                curr += 1
        best = curr
        n = len(blocks)
        for left in range(n - k):
            if blocks[left] == "W":
                curr -= 1
            if blocks[left + k] == "W":
                curr += 1
            best = min(best, curr)
        return best
