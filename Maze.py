options_list = ['Read and load maze from file','View maze','Play maze game','Configure current maze','Export maze to file','Create new maze','Play maze using SenseHAT','View Leaderboard']
points = 0
maze = []
def print_menu(options_list):
    print('MAIN MENU\n=========')
    for i in range(1,len(options_list)+1):
        print("[{}]".format(i),options_list[i-1])
    print()
    print('[0] Exit Maze')
#Option 1 - Read and load maze from file
def load_maze(filename):
    try:
        file = open(filename,'r')
        for line in file:
            line = line.strip('\n')
            mazerow = list(line)
            maze.append(mazerow)
        print('Number of lines read: {}'.format(len(maze)))
        print(maze)
    except FileNotFoundError:
        print('Invalid file. Please Try Again')
        
    
#Option 2 - View Maze
def view_maze(filename):
    for row in maze:
        print(row)

#Option 3 - Play maze game
def play_maze(filename,points): 
    while True:
        print('Option [3] Play maze game\n==========================')
        view_maze(filename)
        print()
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == 'A':
                    print('Location of start (A) = (Row {}, Column {})'.format(row,col))
                    arow = row
                    acol = col
                elif maze[row][col] == 'B':
                    print('Location of end (B) = (Row {}, Column {})'.format(row,col))
                    print()
        movement = input("Press 'W' for UP, 'A' for LEFT, 'S' for down, 'D' for RIGHT, 'M' for Main MENU: ")
        #To go back to Main Menu
        if movement.upper() == 'M':
            break
        #To move up
        elif movement.upper() == 'W':
            if maze[arow-1][acol] == 'O':
                maze[arow-1][acol] = 'A'
                maze[arow][acol] = 'O'
                points = points + 100
            elif maze[arow-1][acol] == 'B':
                complete_maze(points)
                break
            else:
                print('Invalid Move. Please Try Again')
                print()
                points = points - 100
        #To move left
        elif movement.upper() == 'A':
            if maze[arow][acol-1] == 'O':
                maze[arow][acol-1] = 'A'
                maze[arow][acol]= 'O'
                points = points + 100
            elif maze[arow][acol-1] == 'B':
                 complete_maze(points)
                 break
            else:
                print('Invalid Move. Please Try Again')
                print()
                points = points - 100
        #To move down
        elif movement.upper() == 'S':
            if maze[arow+1][acol] == 'O':
                maze[arow+1][acol] = 'A'
                maze[arow][acol]= 'O'
                points = points + 100
            elif maze[arow+1][acol] == 'B':
                complete_maze(points)
                break
            else:
                print('Invalid Movement. Please Try Again')
                print()
                points = points - 100
        #To move right
        elif movement.upper() == 'D':
                if maze[arow][acol+1] == 'O':
                    maze[arow][acol+1] = 'A'
                    maze[arow][acol]= 'O'
                    points = points + 100
                elif maze[arow][acol+1] == 'B':
                    complete_maze(points)
                    break
                else:
                    print('Invalid Movement. Please Try Again')
                    print()
                    points = points - 100


            
#Menu for configuring maze
configlist = ['Create Wall','Create passageway','Create start point','Create end point']
def print_configmenu(configlist):
    print('CONFIGURATION MENU\n==================')
    for i in range(1,len(configlist)+1):
        print('[{}]'.format(i),configlist[i-1])
    print()
    print('[0] Exit to Main Menu')    
#Option 4 - Configure Current Maze
def configure_maze(filename):
    while True:
        print('Option[4] Configure the maze\n==================')
        view_maze(filename)
        print_configmenu(configlist)
        userconfig = int(input('Enter your options: '))
        #To go back to main menu
        if userconfig == 0:
            break
        #To create a wall
        elif userconfig == 1:
                postion = input("Enter the coordinate of the item you wish to change E.g. Row,Column\n'B' to return to configure menu\n'M' to return to main menu: ")
                if postion.upper() == 'M':
                    break
                #To go back to config menu
                elif postion.upper() == 'B':
                    configure_maze(filename)
                    break
                else:
                    try:
                        coords = postion.split(',')
                        maze[int(coords[0])][int(coords[1])] = 'X'
                    except ValueError:
                        print('Please Try again')  
        #To create a passageway  
        elif userconfig == 2:
            postion = input("Enter the coordinate of the item you wish to change E.g. Row,Column\n'B' to return to configure menu\n'M' to return to main menu: ")
            if postion.upper() == 'M':
                break
            elif postion.upper() == 'B':
                configure_maze(filename)
                break
            else:
                try:
                    coords = postion.split(',')
                    maze[int(coords[0])][int(coords[1])] = 'O'
                except ValueError:
                    print('Please Try again')
        #To create a start point
        elif userconfig == 3:
            postion = input("Enter the coordinate of the item you wish to change E.g. Row,Column\n'B' to return to configure menu\n'M' to return to main menu: ")
            if postion.upper() == 'M':
                break
            elif postion.upper() == 'B':
                configure_maze(filename)
                break
            else:
                try:
                    coords = postion.split(',')
                    maze[int(coords[0])][int(coords[1])] = 'A'
                except ValueError:
                    print('Please Try again')
        #To create an end point
        elif userconfig == 4:
            postion = input("Enter the coordinate of the item you wish to change E.g. Row,Column\n'B' to return to configure menu\n'M' to return to main menu: ")
            if postion.upper() == 'M':
                break
            elif postion.upper() == 'B':
                configure_maze(filename)
                break
            else:
                try:
                    coords = postion.split(',')
                    maze[int(coords[0])][int(coords[1])] = 'B'
                except ValueError:
                    print('Please Try again')
#Option 5 - Export maze to file
def export_maze(filename):
    file = open(filename2,'w')
    for row in maze:
        line = ''.join(row)
        file.write('{}\n'.format(str(line)))
    file.close
    print('File {} create with {} records'.format(filename2,len(maze)))
#Option 6 - Create New Maze
def create_maze(row,column):
    maze.clear()
    for i in range(row):
        mazerow = []
        for j in range(column):
            mazerow.append('X')
        maze.append(mazerow)
    print()
    print('A new maze of {} by {} has been created.'.format(row,column)) 
    print('Please run configure maze to start configuring new maze.')  

        
        
#Option 8 - View Leaderboard
leaderboardnames = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7','Player 8','Player 9','Player 10']
score = [2400,1800,1600,1400,1200,1000,800,600,400,200]
def view_leaderboard(leaderboardnames):
    print('{:30s}{:10s}'.format('Name','Score'))
    print('=========================================')
    for i in range(len(score)):
        print('{:30s}{:<10d}'.format(leaderboardnames[i],score[i]))
#Points System
def complete_maze(points):
    print('Congrats! You have completed the maze!')
    name = input('What is your name: ')
    for i in range(len(score)):
        if points>=score[i]:
            leaderboardnames[i] = name
            score[i] = points
            break
        
#To carry out all the function required of the program
while True:
    print_menu(options_list)
    user = int(input('Enter your option: '))
    if user == 0:
        break
    elif user == 1:
        print('Option [1] Read and load maze from file')
        print()
        filename = input('Enter the name of data file: ')
        load_maze(filename)
    elif user == 2:
        print('Option [2] View maze\n==========================')
        view_maze(filename)
    elif user == 3:
        play_maze(filename,points)
    elif user == 4:
        configure_maze(filename)
    elif user == 5:
        print('Option [5] Export maze to file')
        print()
        filename2 = input('Enter filename to save to: ')
        export_maze(filename)
    elif user == 6:
        print('Option [6] Create new maze')
        print()
        decision = input('This will empty the current maze. Are you sure? (Y or N): ')
        print()
        if decision.upper() == 'Y':
            try:
                dimen = input('Enter the dimension of the maze (row,column): ')
                mazedimen = dimen.split(',')
                row = int(mazedimen[0])
                column = int(mazedimen[1])
                create_maze(row,column)
            except ValueError:
                print('Invalid input.Please Try Again')
    elif user == 8:
        print('Option [8] View Leaderboard')
        view_leaderboard(leaderboardnames)
        
    
    


        
 
    





