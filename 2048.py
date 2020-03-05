# Darren Good
# 2020-03-04
# https://open.kattis.com/problems/2048

from sys import stdin

def main():
    inp = stdin.read().strip().split('\n')
    grid = Grid_2048([line.split() for line in inp[0:-1]])

    if (inp[-1] == '0'):
        grid.leftShift()
    elif (inp[-1] == '1'):
        grid.upShift()
    elif (inp[-1] == '2'):
        grid.rightShift()
    else:
        grid.downShift()

    print(grid)


class Grid_2048():
    COLS = 4
    ROWS = 4

    class Tile():
        def __init__(self, value):
            self.val = value
            self.ahead = None
            self.locked = False

        def get_val(self):
            return self.val
        
        def set_val(self, new_val):
            self.val = new_val

        def add_to_val(self, val):
            self.val += val

        def set_ahead(self, tile):
            self.ahead = tile
        
        def shift(self):
            if not self.ahead:
                return
            if (self.ahead.val == 0):
                self.ahead.set_val(self.val)
                self.set_val(0)
                self.ahead.shift()
            elif (self.ahead.val == self.val and not self.ahead.locked):
                self.ahead.add_to_val(self.val)
                self.ahead.lock()
                self.set_val(0)
        
        def lock(self):
            self.locked = True

        def unlock(self):
            self.locked = False

    def __init__(self, grid):
        self.grid = [ [], [], [], [] ]
        for row in range(Grid_2048.ROWS):
            for col in range(Grid_2048.COLS):
                tile = Grid_2048.Tile(int(grid[row][col]))
                self.grid[row].append(tile)
    
    def __str__(self):
        grid_str = ""
        for row in range(Grid_2048.COLS):
            row_str = ""
            for col in range(Grid_2048.COLS): 
                row_str += str(self.grid[row][col].get_val()) + ' '
            grid_str += row_str.rstrip() + '\n'
        return grid_str.rstrip()

        
    def leftShift(self):
        for row in self.grid:
            for i in range(1, Grid_2048.COLS):
                row[i].set_ahead(row[i-1])
            for i in range(1, Grid_2048.COLS):
                row[i].shift()
            for i in range(Grid_2048.COLS):
                row[i].unlock()

    def rightShift(self):
        for row in self.grid:
            for i in range(Grid_2048.COLS - 2, -1, -1):
                row[i].set_ahead(row[i+1])
            for i in range(Grid_2048.COLS - 2, -1, -1):
                row[i].shift()
            for i in range(Grid_2048.COLS):
                row[i].unlock()

    def upShift(self):
        for c in range(Grid_2048.COLS):
            col = [row[c] for row in self.grid]
            for i in range(1, Grid_2048.ROWS):
                col[i].set_ahead(col[i-1])
            for i in range(1, Grid_2048.ROWS):
                col[i].shift()
            for i in range(Grid_2048.ROWS):
                col[i].unlock()
        
    def downShift(self):
        for c in range(Grid_2048.COLS):
            col = [row[c] for row in self.grid]
            for i in range(Grid_2048.ROWS - 2, -1, -1):
                col[i].set_ahead(col[i+1])
            for i in range(Grid_2048.ROWS - 2, -1, -1):
                col[i].shift()
            for i in range(Grid_2048.ROWS):
                col[i].unlock()

main()