from typing import List, Tuple, Optional


class grid_cell_neighborhood:
    """
    grid_cell_neighborhood: class uses: rows, columns, near_value, and active_cell as parameters
    """

    def __init__(self, rows: int, columns: int, near_value: int, active_cell: Optional[List[Tuple[int, int]]] = None) -> None:
        self.rows = rows
        self.columns = columns
        self.n_value = near_value
        self.near_cells = set()
        self.active_cell = active_cell
        self.grid = self.make_grid()


    def count_next_cell(self):
        """
        count_next_cell: loops throught the grid and find all cell containing a 1, 
        then calls helper function close_cell to find all near cells.
        """

        if not self.grid or self.rows == 0 or self.columns == 0:
            print('invalid inputs')
            return 0
        
        for center_row in range(self.rows):
            for center_col in range(self.columns):
                if self.grid[center_row][center_col] == 1:
                    self.close_cell(center_row, center_col)
        
        return len(self.near_cells)

    def close_cell(self, center_row: int, center_col: int):
        """
        close_cell: takes in two parameters(row, col) representing the location of a center cell;
        Use the center cell coordinates and the n_value to generate a mini grid to search all potential near cell in the grid. 
        """
        for cell_row in range(center_row - self.n_value, center_row + self.n_value + 1):
            for cell_col in range(center_col - self.n_value, center_col + self.n_value + 1):

                if 0 <= cell_row < self.rows and 0 <= cell_col < self.columns:
                    # Manhattan Distance formula: d = |x1 - x2| + |y1 - y2|
                    distance = abs(cell_row - center_row) + abs(cell_col - center_col)

                    if distance <= self.n_value:
                        self.near_cells.add((cell_row, cell_col))

    def make_grid(self):
        """
        make_grid: generate grid and mark a cell as positive 
        """
        
        grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

        if self.active_cell:
            for r, c in self.active_cell:
                if 0 <= r < self.rows and 0 <= c < self.columns:
                    grid[r][c] = 1
        else:
            grid[self.rows-1][self.columns-1] = 1

        return grid
    
    def view_final_grid(self):
        """
        view_final_grid: helper function used to run main fuction, count_next_cell, and diplay all near cells
        """

        near_cell_count = self.count_next_cell()
        for r, c in self.near_cells:
             if self.grid[r][c] != 1:
                 self.grid[r][c] = 3
        
        print(f"number of near cells counted: {near_cell_count}" )
        for row in self.grid:
            print("|".join(str(cell) for cell in row))
        print()
        


if __name__ == "__main__":
    # N = 3, active cell = 1
    player_one = grid_cell_neighborhood(11, 11, 3)
    player_one.view_final_grid()

    # N = 3, active cell = 1
    player_one1 = grid_cell_neighborhood(11, 11, 3, [(5, 5)]) 
    player_one1.view_final_grid()

    """ test cases """

    # # N = 3, active cell = 1
    # player_two = grid_cell_neighborhood(11, 11, 3, [(5, 1)]) 
    # player_two.view_final_grid()


    # # N = 2, active cell = 2
    # player_three = grid_cell_neighborhood(11, 11, 2, [(3, 7), (7, 3)]) #
    # player_three.view_final_grid()


    # # N = 2, active cell = 2
    # player_four = grid_cell_neighborhood(11, 11, 2, [(6, 5), (7, 3)]) #
    # player_four.view_final_grid()


    # # N = 2, active cell = 2
    # player_five = grid_cell_neighborhood(11, 11, 2, [(0, 0), (10, 10)]) 
    # player_five.view_final_grid()


    # # N = 0, active cell = 2
    # test_1 = grid_cell_neighborhood(11, 12, 0, [(0, 0), (10, 10)])
    # test_1.view_final_grid()
    
    # # odd shape
    # test_2 = grid_cell_neighborhood(1, 12, 3, [(0, 0), (10, 10)])
    # test_2.view_final_grid()

    # # odd shape
    # test_3 = grid_cell_neighborhood(1, 1, 3, [(0, 0), (10, 10)])
    # test_3.view_final_grid()


    # # N > max(rows, col)
    # test_4 = grid_cell_neighborhood(11, 11, 30, [(0, 0), (10, 10)])
    # test_4.view_final_grid()


