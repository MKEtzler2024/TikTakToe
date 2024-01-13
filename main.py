import turtle as t

Game_Width = 700
Game_Height = 700
Speed = 50
Background_Color = "#000000"

window = t.Screen()
window.title("Tic Tak Toe")
window.setup(width=Game_Width,height=Game_Height)
window.bgcolor(Background_Color)

player =2

pen= t.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0,300)

class X(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.fillcolor("blue")
        self.shape("square")
        self.shapesize(5,5)
        self.penup()
class O(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.fillcolor("red")
        self.shape("circle")
        self.shapesize(5,5)
        self.penup()

class Board(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.fillcolor("red")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=30)
        self.penup()

board1= Board()
board2= Board()
board3= Board()
board4= Board()
board3.shapesize(30,1)
board4.shapesize(30,1)

board1.goto(0,100)
board2.goto(0,-100)
board3.goto(-100,0)
board4.goto(100,0)

#checking winner
# Create the game board
bd = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
def check_winner(bd):
    # Check rows
    for row in bd:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if bd[0][col] == bd[1][col] == bd[2][col] != ' ':
            return bd[0][col]

    # Check diagonals
    if bd[0][0] == bd[1][1] == bd[2][2] != ' ':
        return bd[0][0]

    if bd[0][2] == bd[1][1] == bd[2][0] != ' ':
        return bd[0][2]

    # No winner
    return None

#clicking board
def clicking(x,y):
    global player
    player_turn = "O" if player % 2 == 0 else "X"
    pen.clear()
    pen.write("current player: " + player_turn, align="center", font=('Arial', 24, 'normal'))

    if x < -100 and y > 100:
        if player % 2 == 0:
            x1= X()
            x1.goto(-200,200)
            bd[0][0]="x"
        else:
            x1 = O()
            x1.goto(-200, 200)
            bd[0][0] = "o"
        player += 1
    if (x > -100 and x < 100) and y > 100:
        if player % 2 == 0:
            x1= X()
            x1.goto(0,200)
            bd[0][1] = "x"
        else:
            x1 = O()
            x1.goto(0, 200)
            bd[0][1] = "o"
        player += 1
    if x > 100 and y > 100:
        if player % 2 == 0:
            x1= X()
            x1.goto(200,200)
            bd[0][2] = "x"
        else:
            x1 = O()
            x1.goto(200, 200)
            bd[0][2] = "o"
        player += 1
    if x < -100 and (y > -100 and y < 100):
        if player % 2 == 0:
            x1= X()
            x1.goto(-200,0)
            bd[1][0] = "x"
        else:
            x1 = O()
            x1.goto(-200, 0)
            bd[1][0] = "o"
        player += 1
    if (x > -100 and x < 100) and (y > -100 and y < 100):
        if player % 2 == 0:
            x1= X()
            x1.goto(0,0)
            bd[1][1] = "x"
        else:
            x1 = O()
            x1.goto(0, 0)
            bd[1][1] = "o"
        player += 1
    if x > 100 and (y > -100 and y < 100):
        if player % 2 == 0:
            x1= X()
            x1.goto(200,0)
            bd[1][2] = "x"
        else:
            x1 = O()
            x1.goto(200, 0)
            bd[1][2] = "o"
        player += 1
    if x < -100 and y < -100:
        if player % 2 == 0:
            x1= X()
            x1.goto(-200,-200)
            bd[2][0] = "x"
        else:
            x1 = O()
            x1.goto(-200, -200)
            bd[2][0] = "o"
        player += 1
    if (x > -100 and x < 100) and y < -100:
        if player % 2 == 0:
            x1= X()
            x1.goto(0,-200)
            bd[2][1] = "x"
        else:
            x1 = O()
            x1.goto(0, -200)
            bd[2][1] = "o"
        player += 1
    if x > 100 and y < -100:
        if player % 2 == 0:
            x1= X()
            x1.goto(200,-200)
            bd[2][2] = "x"
        else:
            x1 = O()
            x1.goto(200, -200)
            bd[2][2] = "o"
        player +=1
     # Check for winner
    winner = check_winner(bd)
    if winner:
        pen.clear()
        pen.write("the winner is: " + winner, align="center", font=('Arial', 30, 'normal'))

window.onclick(clicking)

while True:
    window.mainloop()