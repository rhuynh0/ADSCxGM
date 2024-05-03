
import turtle


turtle.up()  # Lift the pen up, so no drawing
turtle.goto(-100, 0)  # Start position
turtle.down()  # Start drawing

# Start drawing the "W"
turtle.right(25)  # Tilt the turtle to start the first leg of W
turtle.forward(100)  # The first leg down
turtle.left(50)  # Angle to start the upward leg
turtle.forward(100)  # First leg up
turtle.right(50)  # Angle to start the downward leg
turtle.forward(100)  # Second leg down
turtle.left(50)  # Angle to start the upward leg
turtle.forward(100)  # Second leg up

    # Finish drawing
    #turtle.hideturtle()  # Hide the turtle icon at the end of drawing

# Set up the turtle environment
