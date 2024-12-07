class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])

        # Stores row, col, steps to gate
        dq = deque()

        # Get all the gates
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    dq.append((row, col, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            row, col, steps = dq.popleft()

            if 0 < rooms[row][col] <= steps:
                continue

            rooms[row][col] = steps
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or rooms[new_row][new_col] <= steps + 1:
                    continue
                dq.append((new_row, new_col, steps + 1))
