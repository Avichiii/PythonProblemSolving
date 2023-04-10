def maze_runner(maze, directions):
    length = len(maze)

    # Find the starting point
    for i in range(length):
        if 2 in maze[i]:
            row = i
            column = maze[row].index(2)
            break
    
    # Follow the directions
    for step in directions:
        if step == 'N': row -= 1
        elif step == 'S': row += 1
        elif step == 'E': column += 1
        elif step == 'W': column -= 1
    
        # Checking Conditions
        if row < 0 or column < 0 or row == length or column == length or maze[row][column] == 1:
            return 'Dead'
        elif maze[row][column] == 3:
            return 'Finish'
    
    return 'Lost'


maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

print(maze_runner(maze, ["N","N","N","N","N","E","E","E","E","E"])) # "Finish"

'''
      0 = Safe place to walk
      1 = Wall
      2 = Start Point
      3 = Finish Point

'''
