class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                box = (row // 3) * 3 + col // 3
                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    print(row, col)
                    print(rows)
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)
        return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        """
        Check whether each row in the sudoku board is valid
        """
        def check_row(board):
            for row in board:
                check = set()
                for ele in row:
                    if ele == ".":
                        continue
                    elif ele in check:
                        return False
                    else:
                        check.add(ele)
            return True

        """
        Check whether each column in the sudoku board is valid
        """
        def check_column(board):
            for i in range(9):
                check = set()
                for j in range(9):
                    ele = board[j][i]
                    if ele == ".":
                        continue
                    elif ele in check:
                        return False
                    else:
                        check.add(ele)
            return True

        """
        Check whether each box in the sudoku board is valid
        """
        def check_box(board):
            # There are 9 boxes on a 9x9 Sudoku board
            for box_start_row in range(0, 9, 3):
                for box_start_col in range(0, 9, 3):
                    check = set()
                    # Each box has 3 rows and 3 columns
                    for row in range(box_start_row, box_start_row + 3):
                        for column in range(box_start_col, box_start_col + 3):
                            ele = board[row][column]
                            if ele == ".":
                                continue
                            if ele in check:
                                return False
                            check.add(ele)
            return True

        if not check_row(board) or not check_column(board) or not check_box(board):
            return False

        return True
