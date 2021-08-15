from sense_hat import SenseHat 
sense = SenseHat()
sense.clear() 
A = [0,255,0]
O = [0,0,0]
B = [255,0,0]
X = [255,255,255]
maze = [X,X,X,X,X,X,X,X, X,O,O,O,X,O,A,X, X,O,X,O,X,O,X,X, X,O,X,O,X,O,O,X, X,O,X,O,X,X,O,X, X,O,X,O,X,O,O,X, X,O,X,O,O,O,X,X, X,B,X,X,X,X,X,X]
flag = True
def joystick_up():
    if maze[apos-8] == O:
        maze[apos-8] = A
        maze[apos] = O
    elif maze[apos-8] == B:
        sense.show_message("Congrats", text_colour=[0,0,255], 
        back_colour=[255,255,0])
        flag = False

def joystick_down():
    if maze[apos+8] == O:
        maze[apos+8] = A
        maze[apos] = O
    elif maze[apos+8] == B:
        sense.show_message("Congrats", text_colour=[0,0,255], 
        back_colour=[255,255,0])
        flag = False
def joystick_left():
    if maze[apos-1] == O:
        maze[apos-1] = A
        maze[apos] = O
    elif maze[apos-1] == B:
        sense.show_message("Congrats", text_colour=[0,0,255], 
        back_colour=[255,255,0])
        flag = False

def joystick_right():
    if maze[apos+1] == O:
        maze[apos+1] = A
        maze[apos] = O
    elif maze[apos+1] == B:
        sense.show_message("Congrats", text_colour=[0,0,255], 
        back_colour=[255,255,0])
        flag = False


while flag:
    for event in sense.stick.get_events():
        for i in range(len(maze)):
            if maze[i] == A:
                apos = i
        if event.action == "pressed":
            sense.set_pixels(maze)
            #Check which direction
            if event.direction == 'up':
               joystick_up()
            elif event.direction == 'down':
               joystick_down()
            elif event.direction == 'left':
               joystick_left()
            elif event.direction == 'right':
                joystick_right()
           


        
 
    





