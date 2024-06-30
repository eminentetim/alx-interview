#!/usr/bin/python3


def island_perimeter(grid):
    # Initialize the perimeter
    perimeter = 0
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is land
            if grid[i][j] == 1:
                # Start by adding 4 to the perimeter for the current land cell
                perimeter += 4
                
                # Check the cell above (if it exists and is land)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                
                # Check the cell below (if it exists and is land)
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                
                # Check the cell to the left (if it exists and is land)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                
                # Check the cell to the right (if it exists and is land)
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
