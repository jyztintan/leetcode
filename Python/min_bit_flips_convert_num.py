class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        # Let the goal always have the longer length
        if len(start) > len(goal):
            start, goal = goal, start
        diff = len(goal) - len(start)
        ans = 0
        for i in range(diff):
            if goal[i] == '1':
                ans += 1
        # We ignore the leading characters since we already counted them
        goal = goal[diff:]
        for i in range(len(start)):
            if start[i] != goal[i]:
                ans += 1
        return ans


print(Solution().minBitFlips(1, 10))
