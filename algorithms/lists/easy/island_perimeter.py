def calculate_island_perimeter(grid):
    last_row = [0] * len(grid[0])
    total_perimeter = 0

    for i in grid:
        last_cell_value = 0
        curr_row = i
        curr_row_perimeter = 0
        for j in range(0, len(curr_row)):
            last_row_cell_value = last_row[j]
            curr_cell_value = curr_row[j]
            if curr_cell_value == 1:
                if last_cell_value == 1:
                    curr_row_perimeter += 2
                else:
                    curr_row_perimeter += 4

                if last_row_cell_value == 1:
                    curr_row_perimeter -= 2

                last_cell_value = curr_cell_value

            else:
                last_cell_value = 0

        total_perimeter += curr_row_perimeter
        last_row = curr_row

    return total_perimeter


if __name__ == '__main__':
    perimeter1 = calculate_island_perimeter([[1, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0]])
    perimeter2 = calculate_island_perimeter([[1]])
    perimeter3 = calculate_island_perimeter([[1, 0]])
    perimeter4 = calculate_island_perimeter([[0, 0]])
    print(perimeter1)
    print(perimeter2)
    print(perimeter3)
    print(perimeter4)
