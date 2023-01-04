from turtle import Turtle

MOVE_DISTANCE = 20
TILE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "white"


class Snake:
    def __init__(self):
        self.tiles = []
        for position in TILE_POSITIONS:
            new_tile = Turtle("square")
            new_tile.color("white")
            new_tile.penup()
            new_tile.goto(position)
            self.tiles.append(new_tile)
        self.head = self.tiles[0]

    def extend(self):
        new_tile = Turtle("square")
        new_tile.color(SNAKE_COLOR)
        new_tile.penup()

        last_tile_xcor = self.tiles[len(self.tiles) - 1].xcor()
        last_tile_ycor = self.tiles[len(self.tiles) - 1].ycor()

        new_tile.goto(last_tile_xcor, last_tile_ycor)
        self.tiles.append(new_tile)

    def move(self):
        for position in range(len(self.tiles) - 1, 0, -1):  # reverse order
            new_x = self.tiles[position - 1].xcor()
            new_y = self.tiles[position - 1].ycor()
            self.tiles[position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        self.head.setheading(UP)

    def go_down(self):
        self.head.setheading(DOWN)

    def go_left(self):
        self.head.setheading(LEFT)

    def go_right(self):
        self.head.setheading(RIGHT)
