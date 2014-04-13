# -*-coding:Utf-8 -*

class Grid():
    """Represents the 'sand table'."""

    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        string = '\n'
        for row in self.grid:
            string = string+row.__str__()+'\n'
        
        return string

    