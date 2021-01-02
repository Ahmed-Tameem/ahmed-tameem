import turtle
import random
import math
import winsound


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Bumpy Boi Game")
wn.bgpic("background.gif")
# wn.register_shape("Player.gif")
# wn.register_shape("minion.gif")


class Player(turtle.Turtle):
    def __init__(self, color = "yellow"):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color(str(color))
        self.shape("triangle")
        self.velocity = 1
        self.speedlimit = 4

    def move(self):
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.goto(0,0)
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
           #self.velocity += 0.5
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
           #self.velocity += 0.5

        if self.velocity > self.speedlimit:
            self.forward(self.speedlimit)
        elif self.velocity < -self.speedlimit:
            self.forward(-self.speedlimit)
        else:
            self.forward(self.velocity)
            
    def turnleft(self):
        self.left(30)
    
    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.velocity += 1

    def decreasespeed(self):
        self.velocity -= 1

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

class Food(turtle.Turtle):
    amount = 4
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.velocity = 1.5
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def regenerate(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.velocity)
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()

class Traps(turtle.Turtle):
    amount = 2
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.velocity = 0.5
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def regenerate(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.velocity)
        if self.xcor() >= 280 or self.xcor() <= -280:
            self.left(60)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.left(60)
        if self.xcor() > 320 or self.xcor() < -320 or self.ycor() > 320 or self.ycor() < -320:
            self.regenerate()
    
class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(0, 0)

    def touch_checker(self, the_player, the_food):
        if (the_player != None):
            x_dis = the_player.xcor() - the_food.xcor()
            y_dis = the_player.ycor() - the_food.ycor()
            distance = math.sqrt((x_dis ** 2) + (y_dis ** 2))
            if distance < 20:
                return True
            else:
                return False

    def update_game_status(self, score1, score2):
        self.goto(0,0)
        if score1 > score2:
            self.write("{}".format("Player 1 Wins"), False, align = "center", font =("Arial", 65, "normal"))
        if score1 < score2:
            self.write("{}".format("Player 2 Wins"), False, align = "center", font =("Arial", 65, "normal"))
        if score1 == score2:
            self.write("{}".format("Draw!"), False, align = "center", font =("Arial", 65, "normal"))

    def game_over(self, the_player, the_traps):
        if (the_player != None):
            x_dis = the_player.xcor() - the_traps.xcor()
            y_dis = the_player.ycor() - the_traps.ycor()
            distance = math.sqrt((x_dis ** 2) + (y_dis ** 2))
            if distance < 20:
                return True
            else:
                return False

    def play_eating_sound(self):
        winsound.Beep(500, 50)

    def play_game_over_sound(self):
        winsound.Beep(2000, 100)

class Score(turtle.Turtle):
    def __init__(self, positionx, positiony, player_num):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(positionx, positiony)
        self.score = 0
        self.player_num = player_num

    def update_score(self):
        self.clear()
        self.write("Score {}: {}".format(self.player_num, self.score), False, align = "left", font =("Arial", 14, "normal"))
    
    def change_score (self, points):
        self.score += points
        self.update_score()


wn.tracer(0)


border = Border()
game = Game()
player1_score = Score(-290, 310, 1)
player2_score = Score(190, 310, 2)

border.draw_border()

player1 = Player("blue")
player2 = Player("purple")

the_food = []

for i in range(Food.amount):
    the_food.append(Food())

the_traps = []

for i in range(Traps.amount):
    the_traps.append(Traps())

player1_score.change_score(0)
player2_score.change_score(0)
game_active1 = 1
game_active2 = 1

turtle.listen()
turtle.onkey(player1.turnleft, "Left")
turtle.onkey(player1.turnright, "Right")
turtle.onkey(player1.increasespeed, "Up")
turtle.onkey(player1.decreasespeed, "Down")
turtle.listen()
turtle.onkey(player2.turnleft, "A")
turtle.onkey(player2.turnright, "D")
turtle.onkey(player2.increasespeed, "W")
turtle.onkey(player2.decreasespeed, "S")
turtle.onkey(player2.turnleft, "a")
turtle.onkey(player2.turnright, "d")
turtle.onkey(player2.increasespeed, "w")
turtle.onkey(player2.decreasespeed, "s")


while game_active1 or game_active2:
    wn.update()
    for food in the_food:
        food.move()
        if game.touch_checker(player1, food):
            food.regenerate()
            game.play_eating_sound()
            player1_score.change_score(10)
        if game.touch_checker(player2, food):
            food.regenerate()
            game.play_eating_sound()
            player2_score.change_score(10)

    for trap  in the_traps:
        trap.move()
        if game.game_over(player1, trap):
            game.play_game_over_sound()
            game_active1 = 0
            player1.hideturtle()
            del player1
            player1 =  None
        if game.game_over(player2, trap):
            game.play_game_over_sound()
            game_active2 = 0
            player2.hideturtle()
            del player2
            player2 = None

    if  game_active1:
        player1.move()
    if game_active2:
        player2.move()

    if not game_active1:
        if player1_score.score < player2_score.score:
            game_active2 = 0

    if not game_active2:
        if player2_score.score < player1_score.score:
            game_active1 = 0

while not game_active1 or not game_active2:
    game.update_game_status(player1_score.score, player2_score.score)





