from turtle import Turtle, Screen
from paddle import Paddle  # Note the uppercase 'Paddle' here
from ball import Ball # Note the uppercase 'Paddle' here
from scoreboard import ScoreBoard


#Creating the screen
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=800, height=500)
my_screen.bgcolor('black')

#Creating the paddles and moving the paddles
l_paddle = Paddle(-390, 0)
r_paddle = Paddle(385, 0)


my_screen.onkey(r_paddle.move_up, "Up")
my_screen.onkey(r_paddle.move_down, "Down")
my_screen.onkey(l_paddle.move_up, "w")  # Note the lowercase 'w' here
my_screen.onkey(l_paddle.move_down, "s")  # Note the lowercase 's' here


my_screen.listen()

#Creating the ball
ball = Ball()

#Creating the scoreboard
scoreboard = ScoreBoard(-350,180)
my_screen.tracer(1)


while True:
    ball.move()
    #bouncing the ball when it touches the top or bottom
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.change_y()        
    #bouncing the ball when it touches the rigth paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 370:
        ball.change_x()     
    #bouncing the ball when it touches the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -370:
        ball.change_x()
        
        
        #when rigth player misses
    if ball.xcor() > 400:
        scoreboard.add_left()
        my_screen.tracer(0)
        ball.reset_ball()
        my_screen.tracer(1)
        
        
    #when left player misses
    if ball.xcor() < -400:
        scoreboard.add_right()
        my_screen.tracer()
        ball.reset_ball()
        my_screen.tracer(1)






#Ensure screen doesnt go off
my_screen.mainloop()
