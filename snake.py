from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in START_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):

        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg_nums in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_nums-1].xcor()
            new_y = self.segments[seg_nums-1].ycor()
            self.segments[seg_nums].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            print("up")

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            print("Down")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            print("right")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            print("left")
