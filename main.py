import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks

# setup the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Create game objects
paddle = Paddle((0, -270))
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

#gaming loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)  # Adjust this for speed

    # Detect collision with bricks
    for brick in bricks.all_bricks:
        if ball.distance(brick) < 35:  # Adjust for size sensitivity
            ball.bounce_y()  # Change direction of the ball
            brick_color = brick.color()[0]  # Extract the color of the brick
            bricks.remove_brick(brick)  # Ensure this properly updates the all_bricks list
            scoreboard.add_points(brick_color)
            break  # Exit the loop after collision to avoid multiple removals

    # Check if all bricks have been hit after handling collisions
    if len(bricks.all_bricks) == 0:
        scoreboard.is_a_win()  # Display win message
        game_is_on = False


    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() < -245:
        ball.bounce_y()

    # Detect ball misses paddle
    if ball.ycor() < -280:  # Ball misses paddle
        scoreboard.decrease_life()
        ball.reset_position()

        # Check if lives are zero after decreasing
        if scoreboard.lives == 0:
            scoreboard.game_over()  # Display game over message
            game_is_on = False
            # screen.listen()
            # screen.onkey(restart_game, "space")

    # Detect collision with left and right walls
    if ball.xcor() > 490 or ball.xcor() < -490:
        ball.bounce_x()

# End the game on click
screen.exitonclick()