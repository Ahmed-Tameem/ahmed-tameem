import turtle
import random
import math
import winsound


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Bumpy Boi Game")
wn.bgpic("background.gif")
wn.register_shape("Player.gif")
wn.register_shape("minion.gif")

class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("Player.gif")
        self.velocity = 1
        

    def move(self):
        if self.velocity > 10:
            self.forward(10)
        elif self.velocity < -10:
            self.forward(-10)
        else:
            self.forward(self.velocity)
            

        if self.xcor() >= 290 or self.xcor() <= -290:
            self.left(60)
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.left(60)

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
        self.color("yellow")
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
        self.shape("minion.gif")
        self.velocity = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def move(self):
        self.forward(self.velocity)

        if self.xcor() >= 290 or self.xcor() <= -290:
            self.left(60)
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.left(60)
    
    def regenerate(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Score : {}".format(self.score), False, align = "left", font =("Arial", 14, "normal"))
    
    def change_score (self, points):
        self.score += points
        self.update_score()



def Touch_checker(the_player, the_food):
    x_dis = the_player.xcor() - the_food.xcor()
    y_dis = the_player.ycor() - the_food.ycor()
    
    distance = math.sqrt((x_dis ** 2) + (y_dis ** 2))

    if distance < 20:
        return True
    else:
        return False


def play_eating_sound():
    winsound.Beep(200, 10)

player = Player()
border = Border()
game = Game()

border.draw_border()

the_food = []

for i in range(Food.amount):
    the_food.append(Food())

turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")
turtle.onkey(player.decreasespeed, "Down")

wn.tracer(0)

game.change_score(0)

while True:
    wn.update()
    player.move()
    for food in the_food:
        food.move()
        if Touch_checker(player, food):
            food.regenerate()
            play_eating_sound()
            game.change_score(10)
            

