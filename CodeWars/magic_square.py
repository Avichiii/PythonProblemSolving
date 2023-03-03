' users have to use the Siamese method for this task'

def magic_square(n):
    # List Compression: where it's storing n number of rows and columns with values 0
    # square = [[0 for _ in range(n)] for _ in range(n)]

    # or this
    
    magic_square_row = []
    for _ in range(n):
        magic_square_column = []
        for _ in range(n):
            magic_square_column.append(0)    
        magic_square_row.append(magic_square_column)
    
    square = magic_square_row

    # Set the starting position
    row = n - 1
    col = n // 2

    # Fill in the square with consecutive numbers
    for i in range(1, n * n + 1):
        square[row][col] = i
        
        # Move to the next position
        row = (row - 1) % n
        col = (col + 1) % n
        
        # If the next position is already filled, move to the position below
        if square[row][col]:
            row = (row + 2) % n
            col = (col - 1) % n

    # rotate the square
    new_square = [square[-1]]
    for row in square[:-1]:
        new_square.append(row)
        
    return new_square


    
print(magic_square(3))
       
    




# magic_square(3)