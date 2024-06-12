class Solution:
    def dailyTemperatures(self, temperatures):
        st = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][1]:
                idx, _ = st.pop()
                res[idx] = i - idx
            st.append((i, temp))
        return res

# sol = Solution()
# temperatures = [73,74,75,71,69,72,76,73]
# print(sol.dailyTemperatures(temperatures))
# temperatures = [30,40,50,60]
# print(sol.dailyTemperatures(temperatures))
# temperatures = [30,60,90]
# print(sol.dailyTemperatures(temperatures))
