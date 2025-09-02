import turtle
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Invalid Input!')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')

def finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()
    y = HEIGHT // 2 - 20
    line.goto(-WIDTH // 2 + 20, y)
    line.pendown()
    line.pensize(4)
    line.color('black')
    line.forward(WIDTH - 40)

def announce_winner(color):
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, 0)
    announcer.color(color)
    announcer.write(f"The winner is {color}!", align="center", font=("Arial", 24, "bold"))

def race(colors):
    turtles = create_turtles(colors)
    finish_y = HEIGHT // 2 - 20
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= finish_y:
                winner_color = colors[turtles.index(racer)]
                announce_winner(winner_color)
                return winner_color

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()
finish_line()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
turtle.done()
