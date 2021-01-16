class player:

    def __init__(self,value,strategy):
        self.value = value
        self.strategy = strategy
    
    def select_move(self,board,actions):
        return self.strategy.SelectMove(board=board,actions=actions,player_value=self.value) #why is self here
    

