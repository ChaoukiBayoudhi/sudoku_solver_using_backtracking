import random as rd
import numpy as np
class SudokuBacktracking:
    def __init__(self,n=0) -> None:
        self.nb_initialized_case=n # number of initialized cases
        self.board=[[0 for _ in range(9)]for _ in range(9)]

    def generate_board(self):
        self.nb_initialized_case=17+rd.random()%(46-17+1)
        #using numpy
        self.nb_initialized_case=np.random.randint(17,46)
        for i in range(self.nb_initialized_case):
            i,j=self.get_random_case()
            val=np.random.randint(1,9)
            while not self.valid_proposition(i,j,val):
                val=np.random.randint(1,9)



    def get_random_case(self):
        ok=True
        while ok:
            i=np.random.randint(0,len(self.board)-1)
            j=np.random.randint(0,len(self.board)-1)
            if self.board[i][j]==0:
                ok=False
        return i,j


    def print_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j],end="\t")

    def valid_proposition(self,indL, indC, val_prop)->bool:
        #verify if the proposition value is not unique on the line
        if val_prop in self.board[indL]:
            return False
        
        #verify if the proposition value is not unique on the line
        i=0
        valid=True
        while i<9 and valid:
            if self.board[i][indC]==val_prop:
                valid=False
            i+=1
        if not valid:
            return False
        #verify the 3x3 square    

    def solve(self):
        pass


#testing
sudoku=SudokuBacktracking()
sudoku.generate_board()
sudoku.print_board()
sudoku.solve()
print("The solved sudoku board is")
sudoku.print_board()
