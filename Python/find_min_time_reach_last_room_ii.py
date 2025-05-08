class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        min_heap = []
        heappush(min_heap, (0, True, 0, 0))  # Time, seq, n, m
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(moveTime), len(moveTime[0])

        while min_heap:
            time, seq, row, col = heappop(min_heap)
            if moveTime[row][col] == -1:  # If processed then ignore
                continue
            moveTime[row][col] = -1  # Lazily mark as visited
            if row == n - 1 and col == m - 1:
                return time
            for x, y in directions:
                new_row, new_col = row + x, y + col
                if 0 <= new_row < n and 0 <= new_col < m and moveTime[new_row][new_col] != -1:
                    if seq:
                        new_time = max(time, moveTime[new_row][new_col]) + 1
                    else:
                        new_time = max(time, moveTime[new_row][new_col]) + 2
                    heappush(min_heap, (new_time, not seq, new_row, new_col))
        return moveTime[-1][-1]
