from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(row, col):
            seen = [False] * 10
            for r in range(3):
                for c in range(3):
                    num = grid[row + r][col + c]
                    if num < 1 or num > 9 or seen[num]:
                        return False
                    seen[num] = True

            d1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            d2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]

            r1 = sum(grid[row][col:col + 3])
            r2 = sum(grid[row + 1][col:col + 3])
            # r3 = sum(grid[row + 2][col:col + 3])

            c1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            c2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            # c3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

            if not (d1 == d2 == r1 == r2 == c1 == c2):
                return False
            return True

        count = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                count += is_magic(row, col)
        return count


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        # If grid does not even have 3 rows and columns then we cannot even get any square (let alone magic)
        if len(grid) < 3 or len(grid[0]) < 3:
            return ans

        def is_magic_square(row, col):
            seen = set()

            MAGIC_SQUARE_SUM = 15 # All magic squares must sum to 15
            row_sums = [0, 0, 0]
            col_sums = [0, 0, 0]

            for i in range(3):
                for j in range(3):
                    curr = grid[row + i][col + j]
                    if curr < 1 or curr > 9:
                        return False
                    if curr in seen:
                        return False
                    seen.add(curr)
                    row_sums[i] += curr
                    col_sums[j] += curr
            if any(x != MAGIC_SQUARE_SUM for x in row_sums) or any(x != MAGIC_SQUARE_SUM for x in col_sums):
                return False

            positive_diagonal = 0
            negative_diagonal = 0
            for i in range(3):
                positive_diagonal += grid[row + 2 - i][col + i]
                negative_diagonal += grid[row + i][col + i]
            return positive_diagonal == MAGIC_SQUARE_SUM and negative_diagonal == MAGIC_SQUARE_SUM

        for row_ptr in range(len(grid) - 2):
            for col_ptr in range(len(grid[0]) - 2):
                if is_magic_square(row_ptr, col_ptr):
                    ans += 1
                col_ptr += 1
            row_ptr += 1

        return ans

# grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# print(Solution().numMagicSquaresInside(grid))
