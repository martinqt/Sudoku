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
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(9):
            for column in range(9):
                if not self.isSet(row, column):
                    self.grid[row][column] = list(choices)

        return 0

    def isSet(self, row, column):
        if isinstance(self.grid[row][column], int) and self.grid[row][column] != 0:
            return True
        else:
            return False

    def setCell(self, row, column, value):
        """Set the value of the cell to a number. Trigger clearing process."""
        self.clearColumn(column, value)
        self.clearRow(row, value)
        self.clearSquare(row, column, value)
        
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

    def initialClear(self):
        """The initial clearing on the all grid."""
        return 0

    def solve(self):
        """Start solving."""
        self.populateUnknown()

        return self.toString()

    def __str__(self):
        return self.toString()