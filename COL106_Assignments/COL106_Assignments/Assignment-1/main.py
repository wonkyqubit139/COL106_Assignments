from maze import *
from navigator import *

def is_valid(x : int, y : int, rows : int, cols : int) -> bool:
    if(x < 0 or x >= rows):
        print("The row of cell", (x, y), "is out of bounds, hence this path is invalid.")
        return False
    elif(y < 0 or y >= cols):
        print("The column of cell", (x, y), "is out of bounds, hence this path is invalid.")
        return False
    return True
def is_neighbour(x1 : int, y1 : int, x2 : int, y2 : int) -> bool:
    return abs(x2-x1) + abs(y2-y1) == 1
if __name__ == "__main__":
    
    ## YOU CAN TWEAK THESE PARAMETERS IN ORDER TO GENERATE MORE TESTCASES
    grid_rows = 16
    grid_cols = 16
    ghosts = [
 (0, 0), (0, 2), (0, 14), 
 (1, 0), (1, 2), (1, 4), (1, 5), (1, 6), (1, 8), (1, 10), (1, 11), (1, 12), (1, 14),
 (2, 0), (2, 4), (2, 8), (2, 10),
 (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15),
 (4, 0), (4, 2), (4, 8),
 (5, 0), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 10), (5, 11), (5, 12), (5, 14), (5, 15),
 (6, 0), (6, 12),
 (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15),
 (8, 0), (8, 2), (8, 6),
 (9, 0), (9, 2), (9, 3), (9, 4), (9, 6), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 14), (9, 15),
 (10, 0), (10, 8),
 (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 14), (11, 15),
 (12, 0), (12, 2), (12, 12),
 (13, 0), (13, 2), (13, 4), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 12), (13, 14), (13, 15),
 (14, 4),
 (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)
]

    start_point = (0,15)
    end_point = (15,0)
    ## This is where the checker logic starts
    sample_grid = Maze(grid_rows, grid_cols)
    for ghost in ghosts:
        sample_grid.add_ghost(ghost[0], ghost[1])
        if(not sample_grid.is_ghost(ghost[0], ghost[1])):
            print("The cell", ghost, "is supposed to contain a ghost, but your program says otherwise!\nTESTCASE FAILED")
            exit(1)
    sample_grid.print_grid()
    '''
    EXPECTED OUTPUT : 
    0 1 0 0
    0 0 0 0
    0 0 1 0
    0 1 0 0
    '''
    PacManInstance = PacMan(sample_grid) 
    try:
        path = PacManInstance.find_path(start_point, end_point) 
        isPathValid = True
        if(path[0] != start_point):
            print("The path is supposed to begin with the tuple", start_point, ", hence this path is invalid.")
            isPathValid = False
        if(path[-1] != end_point):
            print("The path is supposed to end with the tuple", end_point, ", hence this path is invalid.")
            isPathValid = False
        allCells = set()
        for cell in path:
            if(is_valid(cell[0], cell[1], grid_rows, grid_cols) and sample_grid.grid_representation[cell[0]][cell[1]] == 1):
                print("The cell", cell, "that you have in your path is not vacant, hence this path is invalid.")
                isPathValid = False
            if(cell in allCells):
                print("The cell", cell, "that you have in your path is a duplicate cell, hence this path is invalid.")
                isPathValid = False
            allCells.add(cell)
        for i in range(len(path) - 1):
            if(not is_neighbour(path[i][0], path[i][1], path[i+1][0], path[i+1][1])):
                print("Cells", path[i], "and", path[i+1], "are not neighbours, hence this path is invalid.")
                isPathValid = False
        if(isPathValid):
            print("PATH FOUND SUCCESSFULLY!")
        else:
            print("TESTCASE FAILED")
    except (PathNotFoundException):
        print("TESTCASE FAILED. A VALID PATH DOES EXIST BETWEEN THESE TWO LOCATIONS")