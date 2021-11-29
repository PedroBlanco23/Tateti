#Algoritmo utilizado para elegir la posicion en el tateti.
def espaciosVaciosEnTablero(tablero):
  espacios = []
  for i in range(len(tablero)):
    for j in range(len(tablero[0])):
      if tablero[i][j] =="":
        espacios.append((i,j))
  return espacios

def esGanador(tablero, turno):
  winner = False
   # Vertical lines
  if (tablero[0][0] == tablero[0][1] == tablero[0][2] ) and tablero[0][2] == turno:
     winner = True
  elif (tablero[1][0] == tablero[1][1] ==tablero[1][2]) and tablero[1][2] == turno:
     winner = True
  elif (tablero[2][0] == tablero[2][1] ==tablero[2][2] ) and tablero[2][2] == turno:
     winner = True
 # Horizontal lines
  elif (tablero[0][0]== tablero[1][0] == tablero[2][0]) and tablero[2][0] == turno:
    winner = True
  elif (tablero[0][1]== tablero[1][1] ==tablero[2][1] ) and tablero[2][1] == turno:
     winner = True
  elif (tablero[0][2] == tablero[1][2] ==tablero[2][2]) and tablero[2][2] == turno:
    winner = True
# Diagonals
  elif (tablero[0][0]== tablero[1][1] ==tablero[2][2]) and tablero[2][2] == turno:
    winner =True
  elif (tablero[2][0]== tablero[1][1] == tablero[0][2] ) and tablero[0][2] == turno:
    winner = True
  return winner




def tateti(tablero, turno):
  espaciosVacios = espaciosVaciosEnTablero(tablero)
  if esGanador(tablero, "X"):
    return 10
  if esGanador(tablero, "O"):
    return -10
  if len(espaciosVacios) ==0:
    return 0
  if turno == "X":
    valor =-999999
  else :
    valor = 999999

  for espacio in espaciosVacios:
    tablero[espacio[0]][espacio[1]] = turno
    if turno == "X":
      valor = max (valor, tateti(tablero, "O"))
    else:
      valor = min (valor, tateti(tablero, "X"))
    tablero[espacio[0]][espacio[1]] = ""
  return valor

def mejorPosicion(tablero, turno):
  espaciosVacios = espaciosVaciosEnTablero(tablero)
  mejorMovimiento = (-1, -1)
  mejorValor = 999999
  for espacio in espaciosVacios:
    tablero[espacio[0]][espacio[1]] = turno
    valor = tateti(tablero, "X")
    tablero[espacio[0]][espacio[1]] = ""
    if valor <mejorValor:
      mejorValor = valor
      mejorMovimiento = (espacio[0], espacio[1])
  return mejorMovimiento[0], mejorMovimiento[1]


def copiar(board):
  lista = [[] for x in range(len(board))]
  for i in range(len(board)):
    for j in range(len(board[0])):
      lista[i].append(board[i][j].text)
  return lista




def elegirMaquina(board):
  tablero = copiar(board)

  return mejorPosicion(tablero, "O")