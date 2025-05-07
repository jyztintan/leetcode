class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        min_heap = []
        heappush(min_heap, (0, 0, 0))  # Time, n, m
        moveTime[0][0] = -1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(moveTime), len(moveTime[0])

        while min_heap:
            time, row, col = heappop(min_heap)
            if row == n - 1 and col == m - 1:
                return time
            for x, y in directions:
                new_row, new_col = row + x, y + col
                if 0 <= new_row < n and 0 <= new_col < m and moveTime[new_row][new_col] != -1:
                    new_time = max(time, moveTime[new_row][new_col]) + 1
                    heappush(min_heap, (new_time, new_row, new_col))
                    moveTime[new_row][new_col] = -1
        return moveTime[-1][-1]
