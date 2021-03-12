class HumanGame:
    
    
    def __init__(self,board,player1,player2,human_value,two_human=False):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.players = [0,self.player1,self.player2]
        self.human_value = human_value
        self.two_human = two_human

    
    def PlayGame(self):
        CurrentPlayer = self.player1
        j = 1
        move = (0,0)
        while (self.board.still_playing() and self.board.get_winner(*move)==0): #While game is not finished
            
            if not self.two_human:
                if j != (-1*self.human_value):
                    self.board.print_board()
            if self.two_human:
                self.board.print_board()
            actions = self.board.get_valid_actions() #Getting possible moves
            move = CurrentPlayer.select_move(self.board,actions) #Selecting the move
            self.board.update_board(*move,CurrentPlayer.value) #updating board
            j *= -1
            CurrentPlayer = self.players[j]
        
        self.board.print_board()

        if not self.two_human: #Handles the case of human vs AI
            if self.board.get_winner(*move) == (-1*self.human_value):
                print('You lose, as expected...')
            elif self.board.get_winner(*move) == self.human_value:
                print('How did you get this lucky?')
            else:
                print('Draw, play again if you dare')
        
        else: #Handles the case of Human vs Human
            if self.board.get_winner(*move) == (-1*self.human_value):
                print('Player 2 wins! Player 1 must suck')
            elif self.board.get_winner(*move) == self.human_value:
                print('Player 1 wins. Step it up player 2.')
            else:
                print('Draw, expected, boring, next game?')

    def play_many_games(self):
        while True:    # infinite loop
            self.board.ResetBoard()
            self.PlayGame()
            #user_input = str(input("Play again? Y or N ")).lower()
            #if user_input == "n":
            #    break
            break