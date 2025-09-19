class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord('A')
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord('A')
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        cells = formula.split("+")
        total = 0
        for cell in cells:
            if cell[0].isalpha():
                row = int(cell[1:]) - 1
                col = ord(cell[0]) - ord('A')
                total += self.grid[row][col]
            else:
                total += int(cell)
        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
