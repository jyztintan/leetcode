class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        checkpoints = []
        n = len(weights)
        for ptr in range(n - 1):
            checkpoints.append(weights[ptr] + weights[ptr + 1])

        checkpoints.sort()
        min_score = sum(checkpoints[:k - 1])
        max_score = sum(checkpoints[-(k - 1):])
        return max_score - min_score
