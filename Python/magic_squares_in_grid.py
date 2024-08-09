from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        # If grid does not even have 3 rows and columns then we cannot even get any square (let alone magic)
        if len(grid) < 3 or len(grid[0]) < 3:
            return ans

        def is_magic_square(row, col):
            # Check that there are no duplicates
            seen = set()

            row_sums = [0, 0, 0]
            col_sums = [0, 0, 0]
            # Check horizontal sets
            for i in range(3):
                for j in range(3):
                    curr = grid[row + i][col + j]
                    # Handle duplicates
                    if curr in seen:
                        return False
                    else:
                        seen.add(curr)

                    # Handle numbers not in [1,9]
                    if curr < 1 or curr > 9:
                        return False

                    row_sums[i] += curr
                    col_sums[j] += curr

            if any(x != 15 for x in row_sums) or any(x != 15 for x in col_sums):
                return False

            # Check diagonals
            positive_diagonal = 0
            negative_diagonal = 0
            for i in range(3):
                positive_diagonal += grid[row + 2 - i][col + i]
                negative_diagonal += grid[row + i][col + i]

            return positive_diagonal == 15 and negative_diagonal == 15

        row_ptr = 0

        # Going down in row
        while row_ptr + 2 < len(grid):
            col_ptr = 0
            # Going left to right
            while col_ptr + 2 < len(grid[0]):
                # Perform a check for magic square
                if is_magic_square(row_ptr, col_ptr):
                    ans += 1
                col_ptr += 1
            row_ptr += 1

        return ans

# grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# print(Solution().numMagicSquaresInside(grid))
