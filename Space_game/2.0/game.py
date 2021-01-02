"""
#Author:    Ahmed Tameem
#Date:      November ‎22, ‎2019
#Comments:  This updated version of the game adds two player functionality.
"""

from turtle import Turtle, Screen
from random import randint
from winsound import Beep
from time import sleep

class Player(Turtle):
    """Generates the player's avatar and handles the logic of it's movement.

    Attributes:
        velocity (int): Decides how fast the player sprite travels across the screen.
        color (str): Determines the color of the player's avatar.
    """

    def __init__(self, color):
        """Initializes the player's avatar.

        Args:
            color (str): Determines the color of the player's avatar.

        Returns: None.
        """
        Turtle.__init__(self)
        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.speed(0)
        self.color(str(color))
        self.shape("triangle")
        self.velocity = 1

    def move(self):
        """Controls the player's movement.

        Args: None.

        Returns: None.
        """

        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.goto(0,0)  #If the player's avatar is detected outside the border, reset it's position to the center of the screen.
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)   #If the player's avatar touches the right/left border, bounce it off the border at a 60° angle.
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)   #If the player's avatar touches the top/bottom border, bounce it off the border at a 60° angle.

        if self.velocity > 5:
            self.forward(5) #If the player's velocity exceeds 5 set it back to 5 as it's the upper limit.
        elif self.velocity < -5:
            self.forward(-5)    #If the player's velocity is lower than -5 set it back to -5 as it's the upper limit on the speed's magnitude.
        else:
            self.forward(self.velocity) #If the player's velocity is between -5 and 5, keep it the same.

    def turnleft(self):
        """Conrtols the player's orientation.

        Args: None.

        Returns: None.
        """

        self.left(30)   #Shift the player's orientation 30° to the left.

    def turnright(self):
        """Conrtols the player's orientation.

        Args: None.

        Returns: None.
        """

        self.right(30)  #Shift the player's orientation 30° to the right.

    def increasespeed(self):
        """Conrtols the player's speed.

        Args: None.

        Returns: None.
        """

        self.velocity += 1  #Increase the player's veolicity by 1.

    def decreasespeed(self):
        """Conrtols the player's speed.

        Args: None.

        Returns: None.
        """

        self.velocity -= 1  #Decrease the player's veolicity by 1.

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
        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.hideturtle ()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        """Draws the border.

        Args: None.

        Returns: None.
        """

        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.goto(-300,-300)    #Preparing to draw the border by putting the pen at the bottom left of the screen.
        self.pendown()  #Putting the pen down to start drawing the border.
        self.goto(-300,300) #Drawing the border by moving the pen in a square.
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

class Food(Turtle):
    """Generates the food that the player eats for points.

    Attributes:
        velocity (int): Decides how fast the food sprite travels across the screen.
    """

    amount = 4  #The number of food that will be spawned.

    def __init__(self):
        """Initializes the food's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.velocity = 1.5
        self.goto(randint(-250, 250), randint(-250, 250))   #Randomizing where the food spawns.
        self.setheading(randint(0,360)) #Randomizing the direction the food heads towards initially.

    def regenerate(self):
        """Sets the initial location and heading of the food.

        Args: None.

        Returns: None.
        """

        self.goto(randint(-250, 250), randint(-250, 250))   #Randomizing where new food will spawns.
        self.setheading(randint(0,360)) #Randomizing the direction whre new food will head towards initially.

    def move(self):
        """Controls the movement of the food.

        Args: None.

        Returns: None.
        """

        self.forward(self.velocity) #Moving the food forward at it's chosen velocity.

        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)    #If the food touches the right/left border, bounce it off the border at a 60° angle.
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)   #If the food touches the top/bottom border, bounce it off the border at a 60° angle.
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()   #If the food is detected outside the border, spawn a new food to replace it.

class Traps(Turtle):
    """Generates the traps that the player should avoid.

    Attributes:
        velocity (int): Decides how fast the traps sprite travels across the screen.
    """

    amount = 2  #The number of traps that will be spawned.
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
        self.goto(randint(-250, 250), randint(-250, 250))   #Randomizing where the trap spawns.
        self.setheading(randint(0,360)) #Randomizing the direction the trap heads towards initially.

    def regenerate(self):
        """Sets the initial location and heading of the trap.

        Args: None.

        Returns: None.
        """

        self.goto(randint(-250, 250), randint(-250, 250))   #Randomizing where new traps will spawn.
        self.setheading(randint(0,360)) #Randomizing the direction whre new traps will head towards initially.

    def move(self):
        """Controls the movement of the trap.

        Args: None.

        Returns: None.
        """

        self.forward(self.velocity) #Moving the trap forward at it's chosen velocity.

        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)    #If the trap touches the right/left border, bounce it off the border at a 60° angle.
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)   #If the trap touches the top/bottom border, bounce it off the border at a 60° angle.
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()   #If the trap is detected outside the border, spawn a new trap to replace it.

class Game(Turtle):
    """Controls the collision detection and ends the game when a trap is hit.

    Attributes:
        score (int): Keeps track of the player's score.
    """

    def __init__(self):
        """Initializes the game's attributes.

        Args: None.

        Returns: None.
        """

        Turtle.__init__(self)
        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

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

        distance = ((x_dis ** 2) + (y_dis ** 2))**0.5   #Compute the distance between the food and the player.

        return distance < 20    #A collision happens when the distance between the food and the player is less than 20.

    def update_game_status(self, score1, score2):
        """Detects collisions between the player and the food.

        Args:
            score1 (int): Player 1's score.
            score2 (int): Player 2's score.

        Returns: None.
        """

        self.goto(0,0)  #Put the pen at the center of the screen.
        if score1 > score2: #Logic for determining the winner then displaying the appropriate message
            self.write("{}".format("Player 1 Wins"), False, align = "center", font =("Arial", 65, "normal"))
        if score1 < score2:
            self.write("{}".format("Player 2 Wins"), False, align = "center", font =("Arial", 65, "normal"))
        if score1 == score2:
            self.write("{}".format("Draw!"), False, align = "center", font =("Arial", 65, "normal"))

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

        distance = ((x_dis ** 2) + (y_dis ** 2))**0.5   #Compute the distance between the trap and the player.

        return distance < 20    #A collision happens when the distance between the trap and the player is less than 20.

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

class Score(Turtle):
    """Controls the scores of both players.

    Attributes:
        positionx (int): x-coordinate of the player's score.
        positiony (int): y-coordinate of the player's score.
        player_num (int): Specifies the number of the player that will get a score update.
    """

    def __init__(self, positionx, positiony, player_num):
        Turtle.__init__(self)
        self.penup()    #Raising the pen to make sure nothing appears on the screen yet.
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(positionx, positiony)
        self.score = 0
        self.player_num = player_num

    def update_score(self):
        """Updates the score of the player.

        Args: None.

        Returns: None.
        """

        self.clear()    #Erase the current score from the screen.
        self.write("Score : {}".format(self.score), False, align = "left",
        font =("Arial", 14, "normal"))  #Write the new score on the screen.

    def change_score (self, points):
        """Adds points to the player's score and updates it.

        Args:
            points (int): the amount by which the player's score is to be incremented.

        Returns: None.
        """

        self.score += points    #updates the score of the player.
        self.update_score() #Write the updated score to the screen.

def main():
    """Main loop where all the game logic is handled.

        Args: None.

        Returns: None.
    """

    game_window = Screen()
    game_window.bgcolor("black")
    game_window.title("The Bumpy Boi Game")
    game_window.bgpic("background.gif")

    border = Border()
    game = Game()
    player1_score = Score(-290, 310, 1)
    player2_score = Score(190, 310, 2)

    border.draw_border()

    player1 = Player("blue")
    player2 = Player("purple")

    the_food = []   #List of Food objects.

    for _ in range(Food.amount):
        the_food.append(Food()) #Spawning the food onto the screen and adding them to the food list.

    the_traps = []  #List of Trap objects.

    for _ in range(Traps.amount):
        the_traps.append(Traps())   #Spawning the traps onto the screen and adding them to the food list.

    game_window.tracer(0)   #Turn automatic scren updates off for preformance.

    player1_score.change_score(0)   #Start the score at 0.
    player2_score.change_score(0)

    game_active1 = True
    game_active2 = True

    game_window.listen()
    game_window.onkey(player1.turnleft, "Left")  #Turn the player's avatar left when the left button is pressed.
    game_window.onkey(player1.turnright, "Right")
    game_window.onkey(player1.increasespeed, "Up")  #Increase the speed of the player's avatar when the up button is pressed.
    game_window.onkey(player1.decreasespeed, "Down")
    game_window.listen()
    game_window.onkey(player2.turnleft, "A")
    game_window.onkey(player2.turnright, "D")
    game_window.onkey(player2.increasespeed, "W")
    game_window.onkey(player2.decreasespeed, "S")
    game_window.onkey(player2.turnleft, "a")
    game_window.onkey(player2.turnright, "d")
    game_window.onkey(player2.increasespeed, "w")
    game_window.onkey(player2.decreasespeed, "s")

    while game_active1 or game_active2:

        game_window.update()    #Update the game window every loop.

        for food in the_food:
            food.move() #Move the food.
            if player1 is not None and game.touch_checker(player1, food):   #If the player touches a food reset the food's position, play the eating sound, and update the score.
                food.regenerate()
                game.play_eating_sound()
                player1_score.change_score(10)
            if player2 is not None and game.touch_checker(player2, food):
                food.regenerate()
                game.play_eating_sound()
                player2_score.change_score(10)

        for trap  in the_traps:
            trap.move() #Move the trap.
            if player1 is not None and game.game_over(player1, trap):   #If a player's avatar hits a trap take it out of the game.
                game.play_game_over_sound()
                game_active1 = False
                player1.hideturtle()
                del player1
                player1 =  None
            if player2 is not None and game.game_over(player2, trap):
                game.play_game_over_sound()
                game_active2 = False
                player2.hideturtle()
                del player2
                player2 = None

        if  game_active1:
            player1.move()  #Move the player's avatar.
        if game_active2:
            player2.move()

        if not game_active1:    #End the game if player 1's avatar has a lower score than player 1 and it gets hit by a trap.
            if player1_score.score < player2_score.score:
                game_active2 = False

        if not game_active2:    #End the game if player 2's avatar has a lower score than player 2 and it gets hit by a trap.
            if player2_score.score < player1_score.score:
                game_active1 = False

    game.update_game_status(player1_score.score, player2_score.score)   #Display the winner/ a draw.
    sleep(2.5)

if __name__ == "__main__":
    main()
    