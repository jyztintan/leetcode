class Solution:
    def restoreMatrix(self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)
        ans = []
        # Initialise the matrix
        for i in range(m):
            ans.append([0] * n)

        while True:
            # Keep track of lowest in row sum that is not 0
            lowest_row = float("inf")
            lowest_row_index = -1
            for i in range(m):
                if 0 < rowSum[i] < lowest_row:
                    lowest_row = rowSum[i]
                    lowest_row_index = i

            # Keep track of lowest in col sum that is not 0
            lowest_col = float("inf")
            lowest_col_index = -1
            for i in range(n):
                if 0 < colSum[i] < lowest_col:
                    lowest_col = colSum[i]
                    lowest_col_index = i

            # We greedily use the smallest sum whether row or column
            lowest = min(lowest_row, lowest_col)

            # If there was no change in lowest, then all row and column sums are 0
            # Hence, we have finished processing the matrix and can stop
            if lowest == float("inf"):
                break

            # We set the lowest row and lowest column to have the lowest sum
            # As we can be sure that we can put this sum into the matrix without overshooting
            ans[lowest_row_index][lowest_col_index] = lowest
            rowSum[lowest_row_index] -= lowest
            colSum[lowest_col_index] -= lowest

        return ans

# rowSum = [3,8]
# colSum = [4,7]
# print(Solution().restoreMatrix(rowSum, colSum))