class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        total = 0
        for part in parts:
            total += int(part) if part.isdigit() else self.cells.get(part, 0)
        return total