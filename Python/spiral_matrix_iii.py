from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        curr = [rStart, cStart]
        ans = [curr]

        # Check if current position is in the grid
        def in_grid(curr):
            return 0 <= curr[0] < rows and 0 <= curr[1] < cols

        # Keep track of the movement functions so that we can easily toggle between them
        # The idx variable represents the current function we are using
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0

        # The distance in which we move increases after every 2 moves, hence we increment distance after 2 moves
        distance = 1
        moves = 0

        # While we haven't explored the entire grid, we keep moving
        while len(ans) != rows * cols:
            direction = directions[idx]
            for i in range(distance):
                curr = [curr[0] + direction[0], curr[1] + direction[1]]
                if in_grid(curr):
                    ans.append(curr)
            idx = (idx + 1) % 4
            if moves == 1:
                moves = 0
                distance += 1
            else:
                moves += 1

        return ans

# print(Solution().spiralMatrixIII(5, 6, 1, 4))
