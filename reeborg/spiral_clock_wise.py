def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_left()
for i in range(9, 0, -1):
    for j in range(2):
        for k in range(i):
            move()
        turn_right()
