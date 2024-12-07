class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        n = len(candidates)

        def backtrack(curr, remainder, limit):
            if remainder == 0:
                combinations.append(curr.copy())
                return
            elif remainder < 0:
                return

            for idx in range(limit, n):
                possible = candidates[idx]
                curr.append(possible)
                backtrack(curr, remainder - possible, idx)
                curr.pop()

        backtrack([], target, 0)
        return combinations
