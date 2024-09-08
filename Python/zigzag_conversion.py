class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        grid = [[""] * n for _ in range(numRows)]
        down = True
        ptr = 0
        x, y = 0, 0
        while ptr < n:
            grid[x][y] = s[ptr]
            ptr += 1
            if down and x + 1 == numRows:
                down = False
            elif not down and x == 0:
                down = True

            if down:
                x += 1
            else:
                x -= 1
                y += 1

        ans = ""
        for row in grid:
            for c in row:
                if c:
                    ans += c

        return ans

print(Solution().convert("PAYPALISHIRING", 7))

