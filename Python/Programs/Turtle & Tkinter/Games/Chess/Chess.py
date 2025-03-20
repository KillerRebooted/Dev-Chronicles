from turtle import *
from tkinter import PhotoImage
import chess, os

win = Screen()
win.title("Chess")
win.bgcolor("white")
win.tracer(0)

#Function to Draw a Chess Board

def make_chess_board(size):

    chess_board = Turtle()
    chess_board.speed(0)

    fill_box = 1

    x = -(size*3)
    y = size*3

    #Make Chess Board Diagonally

    for iteration in range(15):

        chess_board.pu()

        if iteration < 8:

            chess_board.goto(-(size*4), y-(iteration*size))

        else:

            chess_board.goto(x+((iteration%8)*size), -(size*4))

        chess_board.pd()
        
        chess_board.fillcolor("black" if iteration%2==0 else "white")
        
        chess_board.begin_fill()
        for i in range(2):
            chess_board.seth(90 if i%2==0 else -90)
            for i in range(fill_box*2):
                chess_board.fd(size)
                chess_board.right(90 if i%2==0 else -90)
        chess_board.end_fill()

        fill_box += (1 if iteration<7 else -1)

    del chess_board

#Store Start Position of Turtle

def store_start_pos(x, y, turtle):

    global start_pos, start_loc
    
    start_pos = coord_to_notation(x, y)
    start_loc = turtle.xcor(), turtle.ycor()
    
#Function to Drag a Chess Piece

def drag_piece(x, y, turtle):

    turtle.goto(x, y)

    win.update()

#Function to Center Chess Piece

def center_piece(x, y, turtle):

    global start_pos

    multiples = [i for i in range(-(s*4)+s//2, s*4, s)]
    differences_x = [abs(i-x) for i in multiples]
    differences_y = [abs(i-y) for i in multiples]

    round_x = multiples[differences_x.index(min(differences_x))]
    round_y = multiples[differences_y.index(min(differences_y))]

    turtle.goto(round_x, round_y)

    id = turtle.shape().removeprefix(f"{location}\\").removesuffix(".gif")
    id = chess_ids[id]

    notation = coord_to_notation(round_x, round_y)
    move = start_pos+notation
    
    legal_move = [str(i) for i in list(board.legal_moves) if move == str(i)]
    legal_move = legal_move[0] if legal_move != [] else ""

    if legal_move != "":
        board.push_san(legal_move)

        for i in pieces:
            if i != turtle and i.xcor() == round_x and i.ycor() == round_y:
                i.ht()

    else:

        turtle.goto(start_loc)

    win.update()

#Getting Coordinates to Arrange Chess Pieces

def loc(pos):

    columns = "abcdefgh"
    rows = "12345678"

    x = (-s*4) + (columns.find(pos[0])*s) + s/2
    y = (s*4) - (rows[::-1].find(pos[1])*s) - s/2
    
    return x, y

#Convert Chess Piece Coordinates to Chess Notations

def coord_to_notation(x, y):

    x += s*4
    y += s*4

    x = round(x/(s/2))*(s/2)
    y = round(y/(s/2))*(s/2)

    list_x = [i*s/2 for i in range(1, 17)]
    list_y = [i*s/2 for i in range(1, 17)]

    list_x = list_x[:list_x.index(x)+1]
    list_y = list_y[:list_y.index(y)+1]

    x = len([i for i in range(len(list_x)) if i%2==0])
    y = len([i for i in range(len(list_y)) if i%2==0])

    columns = "abcdefgh"[x-1]
    rows = "12345678"[y-1]

    return columns+rows

s = 70

if s%2 == 0: pass
else: quit()

make_chess_board(s)

pieces = []

#Define Chess Board

board = chess.Board()

#Import Chess Piece Assets

location = f"{__file__.removesuffix(os.path.basename(__file__))}Assets"

for i in os.listdir(location):
    
    smaller = PhotoImage(file=f"{location}\\{i}").subsample(20,20)
    
    win.addshape(f"{location}\\{i}", Shape(f"image", smaller))
    pieces.append(Turtle(f"{location}\\{i}"))

#Arranging Chess Pieces

for i in range(32):

    pieces[i].pu()
    pieces[i].speed(0)

    pos = "abcdefgh"[i%8] + "8712"[i//8]
    pieces[i].goto(loc(pos))

    pieces[i].onclick(lambda x, y, turtle=pieces[i]: store_start_pos(x, y, turtle))
    pieces[i].ondrag(lambda x, y, turtle=pieces[i]: drag_piece(x, y, turtle))
    pieces[i].onrelease(lambda x, y, turtle=pieces[i]: center_piece(x, y, turtle))

#Assigning Chess IDs to Identify Different Types of Chess Pieces

piece_id = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,z1,z2,z3,z4,z5,z6".split(",")
chess_id = list(("RNBQKBNRPPPPPPPP"*2))

chess_ids = dict(zip(piece_id, chess_id))

win.update()

done()