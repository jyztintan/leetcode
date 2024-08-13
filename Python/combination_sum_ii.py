class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        ans = []

        def dfs(pointer, combi, total):
            if total > target:
                return
            if total == target:
                ans.append(combi[:])
                return

            prev = -1
            for i in range(pointer, len(candidates)):
                if candidates[i] == prev:
                    continue
                if total + candidates[i] > target:
                    break
                combi.append(candidates[i])
                dfs(i + 1, combi, total + candidates[i])
                combi.pop()
                prev = candidates[i]

        dfs(0, [], 0)
        return ans
