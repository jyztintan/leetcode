class Solution:
    def combinationSum(self, candidates, target: int):

        ans = []

        def dfs(pointer, combi, total):
            if total == target:
                ans.append(combi[:])
                return
            if pointer >= len(candidates) or total > target:
                return

            combi.append(candidates[pointer])
            dfs(pointer, combi, total + candidates[pointer])
            combi.pop()
            dfs(pointer + 1, combi, total)

        dfs(0, [], 0)
        return ans

# candidates = [2,3,6,7]
# print(Solution().combinationSum(candidates, 7))