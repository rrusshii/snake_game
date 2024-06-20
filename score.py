from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.curr_score = 0
        self.goto(0, 280)
        self.color("white")
        self.write(arg=f"Score = {self.curr_score}", move=False, align="center", font=("Courier", 12, "normal"))
        self.hideturtle()

    def update_score(self):
        self.curr_score += 1
        self.clear()
        self.write(arg=f"Score = {self.curr_score}", move=False, align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 18, "normal"))
