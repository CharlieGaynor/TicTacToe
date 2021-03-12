import copy 
class board():

    def __init__(self):
        self.ResetBoard()
        self.rep = {1: 'O', -1: 'X', 0: '-'}
    #Put board back to default
    def ResetBoard(self):
        self.board = [[0,0,0] for i in range(3)]

    
    def get_winner(self,x,y):
    #Check Rows
        if abs(sum(self.board[x])) == 3:
            return self.board[x][0]

    #Check Columns
        if abs(sum(self.board[j][y] for j in range(3))) == 3:
            return self.board[0][y]

    #check Diagonal
        if (x,y) in ((0,0),(1,1),(2,2)): #might need to replace with (x,y) in [(0,0),(2,2)]
            if abs(sum(self.board[i][i] for i in range(3))) == 3:
                return self.board[1][1]
        if (x,y) in ((0,2),(1,1),(2,0)):
            if abs(sum(self.board[2-i][i] for i in range(3))) == 3:
                return self.board[1][1] #Could maybe combine these but time saved prob small


        return 0 #value to say no winner yet, it could be anything != +- 1

    def still_playing(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return True
        return False
                    

    def get_state(self):
        return str(self.board)
    
    def get_state_list(self):
        return copy.deepcopy(list(self.board))
    
    def get_valid_actions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    actions.append((i,j))
        return actions

    def print_board(self):
        for row in self.board:
            for value in row:
                print(self.rep[value],end = '\t')
            print('\n')
        print('-------------------\n')
    
    def update_board(self,x,y,value):
        self.board[x][y] = value

        

            
            
