def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_forward():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        while not wall_in_front():
            move()
    else:
        turn_left()
        if not wall_in_front():
            move()


is_facing_right = False
while not at_goal():
    # First, make sure the robot will start facing right
    # This block of code is used to avoid the infinite loop
    if not is_facing_right:
        # We are using the only function that can modify the position of the robot
        while not is_facing_north():
            turn_left()
        # After the robot is in default position, turn right
        turn_right()
        is_facing_right = True

    # Now robot can go forward to finish goal
    go_forward()
