from turtle import Turtle, Screen

# we will be creating a class here
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# note in python we always declare a constant with capital letters
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

MOVE_DISTANCE = 20


class Snakegame1:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # class ke name ke agae "." ka prayog krna hai

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # IInd Segment
            new_y = self.segments[seg_num - 1].ycor()  # IInd SEGMENT
            self.segments[seg_num].goto(new_x, new_y)  # THIRD SEGMENT
        self.head.forward(MOVE_DISTANCE)  # Ist SEGMENT

    #### this has been made to change the directions

    def up(self):
        if self.head.heading() != DOWN:  # THIS WILL MAKE SURE THAT WHEN WE PRESS UP AND WE PRESS DOWN IT WILL NOT GO
            # DIRECTLY AS IT BREAKS THE RULE
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
