import copy


class game:

    def __init__(self,board,player1,player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.players = [0,self.player1,self.player2] #this might be silly


    def play_game(self):
        CurrentPlayer = self.player1
        j = 1
        move = (0,0)
        while (self.board.still_playing() and self.board.get_winner(*move)==0):
            actions = self.board.get_valid_actions() #Getting possible moves
            move = CurrentPlayer.select_move(self.board,actions) #Selecting the move
            self.board.update_board(*move,CurrentPlayer.value) #updating board
            j *= -1
            CurrentPlayer = self.players[j]
        return self.board.get_winner(*move)
        #This will finish the game, but wont say who won

    def play_many_games(self,number_games,training=0):
        self.player1wins = 0
        self.player2wins = 0
        self.draws = 0
        for _ in range(number_games):
            self.board.ResetBoard()
            game_state = self.play_game()
            if game_state == 1:
                self.player1wins +=1
            if game_state == -1:
                self.player2wins += 1
            elif game_state == 0:
                self.draws +=1



    def learn_one_game(self):
        CurrentPlayer = self.player1
        AbsentPlayer = self.player2
        state_history = []
        j = 1
        while (True):
            actions = self.board.get_valid_actions() #Getting possible moves
            move = CurrentPlayer.select_move(self.board,actions) #Selecting the move
            self.board.update_board(*move,CurrentPlayer.value) #updating board
            new_state = copy.deepcopy(self.board) #New state of the board
            state_history.append(new_state)
            winner = self.board.get_winner(*move) #Find out if someone has won
            if winner:
                CurrentPlayer.strategy.update(state_history,reward=100)
                AbsentPlayer.strategy.update(state_history,reward=-100)
                break
            if not self.board.still_playing():
                CurrentPlayer.strategy.update(state_history,reward=0)
                AbsentPlayer.strategy.update(state_history,reward=0)
                break
            
            AbsentPlayer = self.players[j]
            j *= -1
            CurrentPlayer = self.players[j]
        return self.board.get_winner(*move)

    def learn_many_games(self,number):
        self.player1wins = 0
        self.player2wins = 0
        self.draws = 0
        for _ in range(number):
            self.board.ResetBoard()
            game_state = self.learn_one_game()
            if game_state == 1:
                self.player1wins +=1
            if game_state == -1:
                self.player2wins += 1
            elif game_state == 0:
                self.draws +=1




            

    def print_stats(self):
        print(f'Player 1 Wins: {self.player1wins}')
        print(f'Player 2 Wins: {self.player2wins}')
        print(f'Draws:         {self.draws}')

