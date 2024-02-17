from random import randrange
import random

def check_win(board, player):
    # Verificar filas
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # Verificar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False


#_____________________
def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


# Ejemplo de uso
board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

movimientos=[1,2,3,4,6,7,8,9] 

def sust(n,player='X'):
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == n:
            board[i][j] = player
        

def jugador():
  while True:           
    mov=input('indica movimiento: ')
    if int(mov) in movimientos:
      break
  sust(mov,'0')
  movimientos.remove(int(mov))
  display_board(board)

def jugador2():
  maquina=random.choice(movimientos)
  sust(str(maquina))
  display_board(board)
  movimientos.remove(maquina)

if __name__ == "__main__":
    print('Juego trés en raya\n Desarrollado por Javier Fiestas Botella')
    display_board(board)
    while len (movimientos)>0:

      print('Turno Jugador')
      jugador()

      if check_win(board, 'X'):
        print("¡La máquina ha ganado!")
      elif check_win(board, '0'):
        print("¡Felicidades! Has ganado.")
            
      print('Turno Máquina')
      jugador2()

      if check_win(board, 'X'):
        print("¡La máquina ha ganado!")
      elif check_win(board, '0'):
        print("¡Felicidades! Has ganado.")