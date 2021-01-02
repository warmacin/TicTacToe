#TICTACTOE
#Objectives = Import numpy , DEF Board ,Display Board , Update player moves , Evaluation 

import numpy as np

position = {'1' : (0,0),
                        '2' : (0,1),
                        '3' : (0,2),
                        '4' : (1,0),
                        '5' : (1,1),
                        '6' : (1,2),
                        '7' : (2,0),
                        '8' : (2,1),
                        '9' : (2,2)
                        }

class Board():
        def __init__(self):
                self.board = np.zeros(shape = (3,3), dtype = int)

        def display_board(self):
                print("Game Status")

                for r in range(3):
                        for c in range(3):
                                if self.board[r][c]== 0:
                                        print("__ |" , end = " ")
                                if self.board[r][c]== 1:
                                        print("X |" , end = " ")
                                if self.board[r][c]== 2:
                                        print("O |", end = " ")
                        print()
                        
class Game(Board):
        def update_player1(self, n):
                row,col = position[n]
                self.board[row][col]= 1

        def update_player2(self, m):
                row, col = position[m]
                self.board[row][col]=2

        def row_check(self):
                for r in range(3):
                        if (self.board[r][0] == 1 and self.board[r][1] == 1 and self.board[r][2] == 1):
                                return 1 
                for r in range(3):
                        if (self.board[r][0] == 2 and self.board[r][1] == 2 and self.board[r][2] == 2):
                                return 2

        def col_check(self):
                for c in range(3):
                        if (self.board[0][c] == 1 and self.board[1][c] == 1 and self.board[2][c] == 1):
                                return 1
                for c in range(3):              
                        if (self.board[0][c]== 2 and self.board[1][c] == 2 and self.board[2][c] == 2):
                                return 2        

        def cross_check(self):
                if (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1):
                        return 1
                
                if(self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1):
                        return 1
                
                if (self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2):
                        return 2
                
                if(self.board[0][2] == 2 and self.board[1][1] == 2 and self.board[2][0] == 2):
                        return 2        

def main():
        
        tic = Game()
        print("Tic Tac Toe Begins!")
        tic.display_board()
        while(1):
                p1_move = input(" Player 1 Choose a position from 1-9: ")
                tic.update_player1(p1_move)
                tic.display_board()

                if(tic.row_check() == 1 or tic.col_check() == 1 or tic.cross_check() == 1):
                        print("Player 1 wins!")
                        break

                p2_move = input('Player 2 Choose a position from 1-9:')
                tic.update_player2(p2_move)
                tic.display_board()

                if(tic.row_check() == 2 or tic.col_check() == 2 or tic.cross_check() == 2):
                        print("Player 2 wins!")
                        break
if __name__== "__main__":                
        main()  
