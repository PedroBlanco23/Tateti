#Import
from guizero import App, Box, PushButton, Text
from backtracking import *
import random
#Funciones


def chequear():
  winner = None
   # Vertical lines
  if (board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text) and board_squares[0][2].text in ["X", "O"]:
     winner = board_squares[0][0].text
  elif (board_squares[1][0].text == board_squares[1][1].text ==board_squares[1][2].text) and board_squares[1][2].text in ["X", "O"]:
     winner = board_squares[1][0].text
  elif (board_squares[2][0].text == board_squares[2][1].text ==board_squares[2][2].text ) and board_squares[2][2].text in ["X", "O"]:
     winner = board_squares[2][0].text
 # Horizontal lines
  elif (board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text) and board_squares[2][0].text in ["X", "O"]:
    winner = board_squares[0][0].text
  elif (board_squares[0][1].text == board_squares[1][1].text ==board_squares[2][1].text ) and board_squares[2][1].text in ["X", "O"]:
     winner = board_squares[0][1].text
  elif (board_squares[0][2].text == board_squares[1][2].text ==board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
    winner = board_squares[0][2].text
# Diagonals
  elif (board_squares[0][0].text == board_squares[1][1].text==board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
    winner = board_squares[0][0].text
  elif (board_squares[2][0].text == board_squares[1][1].text == board_squares[0][2].text ) and board_squares[0][2].text in ["X", "O"]:
    winner = board_squares[0][2].text

  if winner is not None:
    print("GANADOR")
    mensaje.value = winner + " ganó!"
    botonsito.show()
    for i in range(3):
      for j in range(3):
        board_squares[i][j].disable()
  elif movimientos==9:
    mensaje.value ="EMPATE"
    botonsito.show()

def desactivarBotones(board):
  for i in board:
    for boton in i:
      boton.enabled = False

def activarBotones(board):
  for i in board:
    for boton in i:
      if(boton.text == ""):
        boton.enabled = True


def cambiar_jugador():
  global board_squares
  global turn 
  global movimientos
  
  if turn == "X":
    desactivarBotones(board_squares)
    turn = "O"
    mensaje.value="Es turno de "+turn
    if movimientos!=9:
      mensaje.value="Calculando movimiento..."
      x, y = elegirMaquina(board_squares)
      choose_square(x, y)
  else:
    activarBotones(board_squares)
    turn = "X"
    mensaje.value="Es turno de "+turn
    
  

def clear_board():
  new_board=[[None, None, None],
  [None, None, None],
  [None, None, None]]
  
  for x in range(3):
    for y in range(3):
      button = PushButton(board, text= "", grid=[y,x], width=8, height=3, command=choose_square, args=[x, y], enabled=True)
      button_size= 20
      button_color="#F08E79"
      button.font= "Times New Roman"
      new_board[x][y]=button
  return new_board

def choose_square(x, y):
  global movimientos
  movimientos+=1
  board_squares[x][y].text = turn
  board_squares[x][y].disable()
  cambiar_jugador()
  chequear()


def reiniciar():
  global movimientos
  global turn
  global board_squares
  global iniciante
  movimientos=0
  board_squares=clear_board()
  botonsito.hide()
  turn = iniciante
  cambiar_jugador()
  iniciante = turn
#App
app=App("Tatetí")
app.height= 300

#Widgets
iniciante = random.choice(["X", "O"])
turn = iniciante
movimientos=0
board= Box(app, layout="grid")
board_color= "#F08E79"
board_squares=clear_board()

mensaje= Text(app, text="Es turno de "+turn)
botonsito=PushButton(app, text="Presione para reiniciar", command=reiniciar, visible=False)


if (turn == "O"):
  x, y = 0, 0
  choose_square(x, y)
    

#Display
app.display()
