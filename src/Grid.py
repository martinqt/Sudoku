# -*-coding:Utf-8 -*

class Grid():
    """Represents the 'sand table'."""

    def __init__(self, grid):
        self.grid = grid
        self.isSolved = False

    def toString(self):
        string = '\n'
        for row in self.grid:
            string = string+row.__str__()+'\n'

        return string

    def populateUnknown(self):
        """Replace unknown cells with an array of possible choices."""
        return 0

    def setCell(self, row, column, value):
        """Set the value of the cell to a number. Trigger clearing process."""
        return 0

    def clearColumn(self, column, value):
        """Remove value as a possible choice for the column."""
        return 0

    def clearRow(self, row, value):
        """Remove value as a possible choice for the row."""
        return 0

    def clearSquare(self, row, column, value):
        """Remove value as a possible choice for the square."""
        return 0

    def solve(self):
        """Start solving."""
        return self.toString()

    def __str__(self):
        return self.toString()