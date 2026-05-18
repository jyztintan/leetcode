class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        seen = set()
        cleaned = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 0
        x, y = 0, 0
        while (x, y, curr) not in seen:
            print(x, y, curr)
            seen.add((x, y, curr))
            cleaned.add((x, y))
            delta_x, delta_y = directions[curr]
            next_x, next_y = x + delta_x, y + delta_y
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or room[next_x][next_y] == 1:
                curr = (curr + 1) % 4
            else:
                x, y = next_x, next_y
        return len(cleaned)
