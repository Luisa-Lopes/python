import numpy as np 
import sys 
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
#Cria o tabuleiro
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board
#Mostra o Tabuleiro
def printBoard(board):
    print(board)
#Move as peças no tabuleiro   
def move(piece, board, player):
    frase = "Player " + str(player + 1) + " Qual coluna deseja colocar?"
    print(frase)
    col = input()
    tabela = ord(col) 

   #Caso o Input não seja número  
    while (tabela < 48) or (tabela > 56):
        print("Digite um número!")
        col = input()
        tabela = ord(col) 

    col = int(col)

    valida = 1
    while(valida == 1):
        if((col > 0) and (col < COLUMN_COUNT + 1)):
       
            for i in range((ROW_COUNT-1),-1,-1):
                if((board[i][col-1]) == 0):
                    board[i][col-1] = piece
                    return board
            print("Coluna cheia!")
                   
        else:
            print("Não existe essa coluna!")
        
        print("Selecione outra coluna: ") 
        col = int(input())
#Verifica a combinação na horizontal
def horizontal(piece,board):

    for i in range (0, ROW_COUNT): 
        for j in range (0, COLUMN_COUNT - 3): 
            if((board[i][j] == piece) and (board[i][j + 1] == piece) and (board[i][j + 2] == piece) and (board[i][j + 3] == piece)):  
                return 1
    return 0 
#Verifica a combinação na vestical
def vestical(piece,board):
    for j in range(0, COLUMN_COUNT):
        for i in range((ROW_COUNT-1), 3,-1):
            if((board[i][j] == piece) and (board[i - 1][j] == piece) and (board[i - 2][j] == piece) and (board[i - 3][j] == piece)):
                return 1
    return 0
#Varifica a combinação na diagonal primária
def DiagPrim(piece,board):
    for j in range(COLUMN_COUNT-3):
        for i in range(ROW_COUNT-3):
            if (board[i][j] == piece and board[i+1][j+1] == piece and board[i+2][j+2] == piece and board[i+3][j+3] == piece):
                return 1
    return 0 
#Verifica a combinação na Diagonal secundária
def DiagSec(piece,board):
    for j in range(COLUMN_COUNT-3):
        for i in range(3, ROW_COUNT):
            if board[i][j] == piece and board[i-1][j+1] == piece and board[i-2][j+2] == piece and board[i-3][j+3] == piece:
                return 1
    return 0
#Verifica se ganhou             
def checkwin (piece,board):
    piece = int(piece) 
    win = horizontal(piece,board)
    win = win + vestical(piece,board)
    win += DiagPrim(piece, board)
    win += DiagSec(piece, board)
    return win
#Verifica se teve Empate
def checkTie(board):
    for i in range(0 , ROW_COUNT):
        for j in range (0, COLUMN_COUNT):
            if board[i][j] == 0:
                return True
    return False
#Função principal
def main():
    board = create_board()
    printBoard(board)
    endgame = 0
    tie = True

    piece = []
    print("Player 1, escolha o caracter")
    piece.append(input()) 
    print("Player 2, escolha o caracter")
    piece.append(input())
   
    turn = 0

    while((endgame == 0) and (tie == True)):
       
        caracter = piece[turn]
        board = move(caracter, board, turn)
        print(board)
        endgame = checkwin(caracter, board)
        tie = checkTie(board) 
        turn += 1
        turn = turn % 2

    if(endgame == 1):
        frase = "Player " + str(turn) + " venceu!" 
        print(frase)
    else:
        frase = "Sem movimentos !!"
        print(frase)
        print("EMPATE")
    
main()