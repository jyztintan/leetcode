from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 0
        dist = 0
        for c in commands:
            if c == -2:
                curr = (curr - 1) % 4
            elif c == -1:
                curr = (curr + 1) % 4
            else:
                delta_x, delta_y = directions[curr]
                for _ in range(c):
                    if (x + delta_x, y + delta_y) in obstacles:
                        break
                    x += delta_x
                    y += delta_y
                dist = max(dist, abs(x) ** 2 + abs(y) ** 2)
        return dist

# commands = [6, -1, -1, 6]
# obstacles = []
# print(Solution().robotSim(commands, obstacles))
