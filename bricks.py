import random
from turtle import Turtle

class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.brick_data = self.create_brick_data()  # List of positions and colors
        self.create_wall()

    def create_brick_data(self):
        # Define brick positions and fixed row colors
        positions_colors = []
        colors = ["red", "orange", "orange", "yellow", "green", "aqua", "blue"]  # Colors for each row
        x_start = -470  # Adjusted for 1000px width (half of 1000 is 500)
        y_start = 200
        brick_width = 100  # Updated width to fit 1000px screen
        brick_height = 20  # Height of each brick remains the same
        row_spacing = 21  # Increase spacing between rows to avoid overlap

        for row in range(7):  # 7 rows, one for each color
            for col in range(16):  # 16 columns
                x_position = x_start + col * brick_width
                y_position = y_start - row * row_spacing
                color = colors[row]  # Set color based on row
                positions_colors.append(((x_position, y_position), color))

        return positions_colors

    def create_wall(self):
        # Create a wall of bricks using the brick data
        for (x, y), color in self.brick_data:
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1, stretch_len=5)  # Stretch to 100 pixels wide
            new_brick.penup()
            new_brick.color(color)
            new_brick.goto(x, y)
            self.all_bricks.append(new_brick)

    def remove_brick(self, brick):
        if brick in self.all_bricks:
            brick.hideturtle()  # Hide the brick
            self.all_bricks.remove(brick)  # Remove from the list

    def reset_wall(self):
        # Hide and remove all existing bricks
        for brick in self.all_bricks:
            brick.hideturtle()  # Hide each brick
        self.all_bricks.clear()  # Clear the list of bricks
        self.brick_data = self.create_brick_data()  # Recreate brick data
        self.create_wall()  # Create the wall again
