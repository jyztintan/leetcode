from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(num):
            row = n - 1 - (num // n)
            col = num % n if (num // n) % 2 == 0 else n - 1 - (num % n)
            return row, col

        visited = [False] * (n * n)
        q = deque()
        q.append([0, 0])

        while q:
            curr, rolls = q.popleft()
            if curr == n * n - 1:
                return rolls
            for incr in range(1, 7):
                nxt = curr + incr
                if nxt >= n * n:
                    break
                row, col = get_position(nxt)
                destination = board[row][col] - 1 if board[row][col] != -1 else nxt
                if not visited[destination]:
                    visited[destination] = True
                    q.append((destination, rolls + 1))
        return -1
