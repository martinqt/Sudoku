# -*-coding:Utf-8 -*

class colors:
    """Helper class to store ansi code."""
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'

class Grid():
    """Represent the Sodoku grid."""

    def __init__(self, grid):
        self.grid = grid
        self.isSolved = False

    def toString(self, raw):
        """Generate the string representation of the grid."""
        if raw == False:
            string = colors.okblue+'\n-------------\n'+colors.end

            for row in range(9):
                for column in range(9):
                    if column%3 == 0:
                        string += colors.okblue+'|'+colors.end

                    if isinstance(self.get(row, column), int):
                        string += colors.okgreen+str(self.get(row, column))+colors.end
                    else:
                        string += colors.header+'?'+colors.end

                if column == 8:
                    string += colors.okblue+'|'+colors.end

                if row%3 == 2:
                    string += colors.okblue+'\n-------------\n'+colors.end
                else:
                    string += '\n'
        else:
            string = '\n'
            for row in self.grid:
                string += row.__str__()+'\n'

        return string

    def populateUnknown(self):
        """Replace unknown cells with an array of possible choices."""
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in range(9):
            for column in range(9):
                if not self.isSet(row, column):
                    self.grid[row][column] = list(choices)

        return 0

    def get(self, row, column):
        """Get the requested cell."""
        return self.grid[row][column]

    def isSet(self, row, column):
        """Check if the given cell is still unknown."""
        if isinstance(self.get(row, column), int) and self.get(row, column) != 0:
            return True
        else:
            return False

    def setCell(self, row, column, value):
        """Set the value of the cell to a number. Trigger clearing process."""
        self.grid[row][column] = value
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
        for row in range(9):
            for column in range(9):
                if self.isSet(row, column):
                    self.setCell(row, column, self.get(row, column))

        return 0

    def solve(self):
        """Start solving."""
        self.populateUnknown()

        return self.toString(False)

    def __str__(self):
        return self.toString(True)