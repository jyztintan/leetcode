from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        latitude, longitude = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        obstacles = set(tuple(obstacle) for obstacle in obstacles)
        furthest = 0
        for command in commands:
            if command > 0:
                # Move robot but check for obstacles
                x, y = directions[curr_dir]
                for i in range(command):
                    new_x, new_y = latitude + x, longitude + y
                    if (new_x, new_y) in obstacles:
                        break
                    furthest = max(furthest, new_x ** 2 + new_y ** 2)
                    latitude, longitude = new_x, new_y

            elif command == -2:
                curr_dir = (curr_dir + 3) % 4
            else:
                curr_dir = (curr_dir + 1) % 4

        return furthest


# commands = [6, -1, -1, 6]
# obstacles = []
# print(Solution().robotSim(commands, obstacles))
