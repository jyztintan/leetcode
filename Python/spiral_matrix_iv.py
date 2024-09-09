# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        grid = [[0] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while left <= right and top <= bottom:
            # Fill top row
            for i in range(left, right + 1):
                if head:
                    grid[top][i] = head.val
                    head = head.next
                else:
                    grid[top][i] = -1
            top += 1
            # Fill right-most col
            for i in range(top, bottom + 1):
                if head:
                    grid[i][right] = head.val
                    head = head.next
                else:
                    grid[i][right] = -1
            right -= 1
            # Fill bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if head:
                        grid[bottom][i] = head.val
                        head = head.next
                    else:
                        grid[bottom][i] = -1
                bottom -= 1
            # Fill left-most col
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if head:
                        grid[i][left] = head.val
                        head = head.next
                    else:
                        grid[i][left] = -1
                left += 1

        return grid


list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().spiralMatrix(3, 3, list))


class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        grid = [[0] * n for _ in range(m)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_ptr = 0
        row_limit = [0, m - 1]
        col_limit = [0, n - 1]
        curr_row, curr_col = 0, 0

        count = 0
        while count != m * n:
            count += 1
            if head:
                grid[curr_row][curr_col] = head.val
                head = head.next
            else:
                grid[curr_row][curr_col] = -1

            # Get the next potential point, assuming moving in the same direction
            next_row = curr_row + directions[dir_ptr][0]
            next_col = curr_col + directions[dir_ptr][1]

            # Check if at boundary, change direction
            if next_row < row_limit[0] or next_row > row_limit[1] or next_col < col_limit[0] or next_col > col_limit[1]:
                match dir_ptr:
                    case 0:
                        row_limit[0] += 1
                    case 1:
                        col_limit[1] -= 1
                    case 2:
                        row_limit[1] -= 1
                    case 3:
                        col_limit[0] += 1

                dir_ptr = (dir_ptr + 1) % 4
                next_row = curr_row + directions[dir_ptr][0]
                next_col = curr_col + directions[dir_ptr][1]

            curr_row, curr_col = next_row, next_col

        return grid


list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().spiralMatrix(3, 3, list))

