"""
#Author:    Ahmed Tameem
#Date:      November ‎11, ‎2019
#Comments:  This was my first software project.  While it was very short, it
#   served as a nice introduction
#   to OOP and was lots of fun to make and play.
"""

from turtle import Turtle, Screen
from random import randint
from winsound import Beep

class Player(Turtle):
    """Generates the player's avatar and handles the logic of it's movement.

    Attributes:
        velocity (int): Decides how fast the player sprite travels across the screen.
    """

    def __init__(self):
        """Initializes the player's avatar.

        Args: None.

        Returns: None.
        """
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("yellow")
        self.shape("triangle")
        self.velocity = 1

    def move(self):
        """Controls the player's movement.

        Args: None.

        Returns: None.
        """

        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.goto(0,0)
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
            # self.velocity += 0.5
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
            # self.velocity += 0.5

        if self.velocity > 5:
            self.forward(5)
        elif self.velocity < -5:
            self.forward(-5)
        else:
            self.forward(self.velocity)

    def turnleft(self):
        """Conrtols the player's orientation.

        Args: None.

        Returns: None.
        """

        self.left(30)

    def turnright(self):
        """Conrtols the player's orientation.

        Args: None.

        Returns: None.
        """

        self.right(30)

    def increasespeed(self):
        """Conrtols the player's speed.

        Args: None.

        Returns: None.
        """

        self.velocity += 1

    def decreasespeed(self):
        """Conrtols the player's speed.

        Args: None.

        Returns: None.
        """

        self.velocity -= 1

class Border(Turtle):
    """Generates the border of the game.

    Attributes: None.
    """

    def __init__(self):
        """Initializes the border's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        """Draws the border.

        Args: None.

        Returns: None.
        """

        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

class Food(Turtle):
    """Generates the food that the player eats for points.

    Attributes:
        velocity (int): Decides how fast the food sprite travels across the screen.
    """

    amount = 4
    def __init__(self):
        """Initializes the food's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.velocity = 1.5
        self.goto(randint(-250, 250), randint(-250, 250))
        self.setheading(randint(0,360))

    def regenerate(self):
        """Sets the initial location and heading of the food.

        Args: None.

        Returns: None.
        """

        self.goto(randint(-250, 250), randint(-250, 250))
        self.setheading(randint(0,360))

    def move(self):
        """Controls the movement of the food.

        Args: None.

        Returns: None.
        """

        self.forward(self.velocity)

        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()

class Traps(Turtle):
    """Generates the traps that the player should avoid.

    Attributes:
        velocity (int): Decides how fast the traps sprite travels across the screen.
    """

    amount = 2
    def __init__(self):
        """Initializes the trap's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.velocity = 0.5
        self.goto(randint(-250, 250), randint(-250, 250))
        self.setheading(randint(0,360))

    def regenerate(self):
        """Sets the initial location and heading of the trap.

        Args: None.

        Returns: None.
        """

        self.goto(randint(-250, 250), randint(-250, 250))
        self.setheading(randint(0,360))

    def move(self):
        """Controls the movement of the trap.

        Args: None.

        Returns: None.
        """

        self.forward(self.velocity)

        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()

class Game(Turtle):
    """Controls the score, collision detection, and ends the game when a trap is hit.

    Attributes:
        score (int): Keeps track of the player's score.
    """

    def __init__(self):
        """Initializes the game's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        """Updates the score of the player.

        Args: None.

        Returns: None.
        """

        self.clear()
        self.write("Score : {}".format(self.score), False, align = "left",
        font =("Arial", 14, "normal"))

    def change_score (self, points):
        """Adds points to the player's score and updates it.

        Args:
            points (int): the amount by which the player's score is to be incremented.

        Returns: None.
        """

        self.score += points
        self.update_score()

    @staticmethod
    def touch_checker(the_player, the_food):
        """Detects collisions between the player and the food.

        Args:
            the_player (Player): The object which has the attribute of the player's coordinates.
            the_food (Food): The object which has the attribute of the food's coordinates.

        Returns:
            (bool): True if there is a collision, False otherwise.
        """

        x_dis = the_player.xcor() - the_food.xcor()
        y_dis = the_player.ycor() - the_food.ycor()

        distance = ((x_dis ** 2) + (y_dis ** 2))**0.5

        return distance < 20

    def update_game_status(self):
        """Displays the "Game Over" message.

        Args: None.

        Returns: None.
        """

        self.goto(0,0)
        self.write("{}".format("Game Over"), False, align = "center", font =("Arial", 75, "normal"))

    @staticmethod
    def game_over(the_player, the_trap):
        """Detects collisions between the player and traps.

        Args:
            the_player (Player): The object which has the attribute of the player's coordinates.
            the_trap (Trap): The object which has the attribute of the trap's coordinates.

        Returns:
            (bool): True if there is a collision, False otherwise.
        """

        x_dis = the_player.xcor() - the_trap.xcor()
        y_dis = the_player.ycor() - the_trap.ycor()

        distance = ((x_dis ** 2) + (y_dis ** 2))**0.5

        return distance < 20

    @staticmethod
    def play_eating_sound():
        """Plays the eat sound.

        Args: None.

        Returns: None.
        """

        Beep(200, 10)

    @staticmethod
    def play_game_over_sound():
        """Plays the sound associated with the game ending.

        Args: None.

        Returns: None.
        """
        Beep(2000, 50)

def main():
    """Main loop where all the game logic is handled.

        Args: None.

        Returns: None.
    """
    game_window = Screen()
    game_window.bgcolor("black")
    game_window.title("The Bumpy Boi Game")
    game_window.bgpic("background.gif")

    player = Player()
    border = Border()
    game = Game()

    border.draw_border()

    the_food = []

    for _ in range(Food.amount):
        the_food.append(Food())

    the_traps = []

    for _ in range(Traps.amount):
        the_traps.append(Traps())


    game_window.listen()
    game_window.onkey(player.turnleft, "Left")
    game_window.onkey(player.turnright, "Right")
    game_window.onkey(player.increasespeed, "Up")
    game_window.onkey(player.decreasespeed, "Down")

    game_window.tracer(0)

    game.change_score(0)

    game_active = True

    while game_active:
        game_window.update()
        player.move()
        for food in the_food:
            food.move()
            if game.touch_checker(player, food):
                food.regenerate()
                game.play_eating_sound()
                game.change_score(10)
        for trap  in the_traps:
            trap.move()
            if game.game_over(player, trap):
                game.play_game_over_sound()
                game_active = False

    while not game_active:
        game.update_game_status()

if __name__ == "__main__":
    main()
    