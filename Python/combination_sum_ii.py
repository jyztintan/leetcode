class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        ans = []

        def dfs(pointer, combi, total):
            if total == target:
                ans.append(combi[:])
                return
            if pointer >= len(candidates) or total > target:
                return

            combi.append(candidates[pointer])
            dfs(pointer + 1, combi, total + candidates[pointer])
            combi.pop()

            while pointer < len(candidates) and candidates[pointer - 1] == candidates[pointer]:
                pointer += 1
            dfs(pointer + 1, combi, total)

        dfs(0, [], 0)
        return ans