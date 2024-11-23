from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        rotated = [['.'] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rotated[j][m - i - 1] = box[i][j]

        for row in range(n - 1, -1, -1):
            for col in range(m):
                if rotated[row][col] == '#':
                    r = row
                    # Move the current leave down as much as possible
                    while r + 1 < n and rotated[r + 1][col] == '.':
                        rotated[r + 1][col] = rotated[r][col]
                        rotated[r][col] = '.'
                        r += 1
        return rotated


# box = [["#",".","*","."],["#","#","*","."]]
# print(Solution().rotateTheBox(box))