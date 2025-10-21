import time
import os
import random

class GameOfLife:
    def __init__(self, rows=12, cols=12):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()

    def create_grid(self):
        """ Generating a grid with live (1) and dead (0) cells"""
        return [[random.choice([0, 1]) for _ in range(self.cols)] for _ in range(self.rows)]

    def display(self):
        """Displaying the grid"""
        os.system('cls' if os.name == 'nt' else 'clear')  # clear console
        for row in self.grid:
            print(' '.join('⬜' if cell == 1 else '⬛' for cell in row))
        print()

    def count_neighbors(self, x, y):
        """Counting live neighbors around cell (x, y)"""
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                count += self.grid[nx][ny]
        return count

    def next_generation(self):
        """Applying the rules of the Game of Life to produce the next generation"""
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                live_neighbors = self.count_neighbors(x, y)
                if self.grid[x][y] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[x][y] = 0  # dies
                    else:
                        new_grid[x][y] = 1  # stays alive
                else:
                    if live_neighbors == 3:
                        new_grid[x][y] = 1  # becomes alive
        self.grid = new_grid

    def run(self, generations=20, delay=0.4):
        """Run the simulation"""
        for gen in range(generations):
            print(f"Generation {gen+1}")
            self.display()
            self.next_generation()
            time.sleep(delay)

# Run the Game of Life with a 12x12 grid
game = GameOfLife(12, 12)
game.run(generations=30, delay=0.3)
