__author__ = 'sylwia'

glob_neighbour_points = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
glob_grid = ()


def calculate_new_coordinates(row, col, move_r, move_c):
    x = row + move_r
    y = col + move_c
    return x, y


def in_grid(coordinates):
    global glob_grid

    value_row = True if 0 <= coordinates[0] < len(glob_grid) else False
    value_col = True if 0 <= coordinates[1] < len(glob_grid[0]) else False

    if value_row and value_col:
        return True

    return False


def check_neighbour(coordinates):
    global glob_grid
    if glob_grid[coordinates[0]][coordinates[1]] == 1:
        return 1
    return 0


def count_neighbours(grid, row, col):

    global glob_grid
    glob_grid = grid

    global glob_neighbour_points
    neighbours_counter = 0

    for point in glob_neighbour_points:
        new_coordinates = calculate_new_coordinates(row, col, point[0], point[1])
        if in_grid(new_coordinates):
            neighbours_counter += check_neighbour(new_coordinates)
    return neighbours_counter


print count_neighbours(((1,0,1,0,1),
                        (0,1,0,1,0),
                        (1,0,1,0,1),
                        (0,1,0,1,0),
                        (1,0,1,0,1),
                        (1,0,1,0,1),), 5, 4)
print count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0)
print count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2)
print count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1)