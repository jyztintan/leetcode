class Solution:
    def lexicalOrder(self, n: int):
        ans = []

        def dfs(num):
            if num > n:
                return
            ans.append(num)
            for i in range(10):
                dfs(num * 10 + i)

        for num in range(1, 10):
            dfs(num)

        return ans

# print(Solution().lexicalOrder(13))
