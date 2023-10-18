from turtle import Turtle

class ScoreBoard(Turtle):
    """Creating the scoreboard for the ping_pong game"""

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.l_player = 0
        self.r_player = 0
        self.write(f"{self.l_player}:{self.r_player}", font= ('segoe UI', 40, 'normal'))
       
    def add_right(self):
        """add 1 to the right player score"""
        self.clear()
        self.r_player += 1
        self.write(f"{self.l_player}:{self.r_player}", font= ('segoe UI', 40, 'normal'))


    def add_left(self):
        """add 1 to the left player score"""
        self.clear()
        self.r_player += 1
        self.write(f"{self.l_player}:{self.r_player}", font= ('segoe UI', 40, 'normal'))
