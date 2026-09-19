class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        highest = 0
        ans = []
        n = len(heights)
        for i in range(n - 1, -1, -1):
            if heights[i] > highest:
                ans.append(i)
                highest = heights[i]
        ans.reverse()
        return ans
