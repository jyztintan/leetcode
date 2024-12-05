class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_idx = stack.pop()
                ans[prev_idx] = idx - prev_idx
            stack.append((temp, idx))
        return ans
