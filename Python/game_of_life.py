# Time complexity: O(M * N)
# O(1) space complexity since we modify everything in place. We big-brain this by using a temp state and iterate again
# to replace this temp state with the correct final state. This doesn't affect time complexity since it is just another
# O(M * N) loop
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                live_neighbours = 0
                for x, y in neighbours:
                    new_row, new_col = row + x, col + y
                    '''
                    0 if processed/not and remains dead
                    1 if yet to be processed and was a live neighbour
                    2 if processed and becomes alive
                    3 if was alive and now died
                    '''
                    if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                        continue
                    if board[new_row][new_col] == 1 or board[new_row][new_col] == 3:
                        live_neighbours += 1

                if board[row][col] == 0 and live_neighbours == 3:
                    board[row][col] = 2
                elif board[row][col] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[row][col] = 3

        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0


