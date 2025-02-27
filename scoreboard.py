from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0  # Initialize the total score
        self.lives = 5  # Start with 5 lives
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Display the score and lives at the top
        self.goto(-150, 225)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 40, "normal"))
        self.goto(150, 225)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 40, "normal"))

    def add_points(self, brick_color):
        # Add points based on the color of the brick
        if brick_color in ["red", "orange"]:
            self.score += 7
        elif brick_color in ["green", "yellow"]:
            self.score += 4
        elif brick_color in ["aqua", "blue"]:
            self.score += 1
        self.update_scoreboard()

    def decrease_life(self):
        # Decrease lives by 1
        self.lives -= 1
        self.update_scoreboard()

        # Check if the player has no lives left
        if self.lives == 0:
            return True

    def game_over(self):
        self.game_active = False  # Set game to inactive
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 60, "bold"))
        # self.goto(0, -50)
        # self.write("Press SPACE to restart", align="center", font=("Courier", 30, "normal"))

    def restart_game(self):
        self.score = 0
        self.lives = 5
        self.game_active = True
        self.update_scoreboard()

    def is_a_win(self):
        self.game_active = False  # Set game to inactive
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 60, "bold"))

