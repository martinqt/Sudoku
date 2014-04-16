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
        self.solved = False
        self.notFound = 0
        self.initial = 0

    def toString(self, raw):
        """Generate the string representation of the grid."""
        string = 'Status: '

        if self.solved == True:
            string += colors.okgreen+'Solved ('+str(self.initial)+')'+colors.end
        else:
            string += colors.fail+'Unsolved ('+str(self.notFound)+'/'+str(self.initial)+')'+colors.end

        string += '\n'

        if raw == False:
            string += colors.okblue+'\n-------------\n'+colors.end

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
            string += '\n'
            for row in self.grid:
                string += row.__str__()+colors.header+'|'+colors.end+'\n'

        return string

    def populateUnknown(self):
        """Replace unknown cells with an array of possible choices."""
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in range(9):
            for column in range(9):
                if not self.isSet(row, column):
                    self.grid[row][column] = list(choices)
                    self.initial += 1

        return 0

    def removeFromList(self, mlist, value):
        return [val for val in mlist if val != value]

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
        for row in range(9):
            if not self.isSet(row, column):
                self.grid[row][column] = self.removeFromList(self.get(row, column), value)

        return 0

    def clearRow(self, row, value):
        """Remove value as a possible choice for the row."""
        for column in range(9):
            if not self.isSet(row, column):
                self.grid[row][column] = self.removeFromList(self.get(row, column), value)

        return 0

    def clearSquare(self, row, column, value):
        """Remove value as a possible choice for the square."""
        rows = []
        columns = []

        left = top = [0, 1, 2]
        center = middle = [3, 4, 5]
        right = bottom = [6, 7, 8]

        #Top rows
        if row in top and column in left:
            rows = top
            columns = left
        elif row in top and column in center:
            rows = top
            columns = center
        elif row in top and column in right:
            rows = top
            columns = right
        #Middle rows
        if row in middle and column in left:
            rows = middle
            columns = left
        elif row in middle and column in center:
            rows = middle
            columns = center
        elif row in middle and column in right:
            rows = middle
            columns = right
        #Bottom rows
        if row in bottom and column in left:
            rows = bottom
            columns = left
        elif row in bottom and column in center:
            rows = bottom
            columns = center
        elif row in bottom and column in right:
            rows = bottom
            columns = right

        for y in rows:
            for x in columns:
                if not self.isSet(y, x):
                    self.grid[y][x] = self.removeFromList(self.get(y, x), value)
        
        return 0

    def initialClear(self):
        """The initial clearing on the all grid."""
        for row in range(9):
            for column in range(9):
                if self.isSet(row, column):
                    self.setCell(row, column, self.get(row, column))

        return 0

    def simplify(self):
        """Remove list of choices with only one choice and check if the grid has been solved (for now)."""
        self.notFound = 0
        for row in range(9):
            for column in range(9):
                if not isinstance(self.get(row, column), int):
                    if len(self.get(row, column)) == 1:
                        self.setCell(row, column, int(self.get(row, column)[0]))
                    else:
                        self.notFound += 1

        if self.notFound == 0:
            self.solved = True
        else:
            self.solved = False

        return 0

    def validate(self):
        """Check if the grid has been solved."""
        return 0

    def solve(self):
        """Start solving."""
        self.populateUnknown()
        self.initialClear()
        
        i = 0
        while i<10 and self.solved == False:
            self.simplify()
            i += 1
        
        return self.toString(False)

    def __str__(self):
        return self.toString(True)