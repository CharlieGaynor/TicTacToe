import random
from collections import defaultdict
import copy
from icecream import ic

class Human():

    def SelectMove(self,board,actions,player_value):
        while True:
            x = (int(input('Select a move, 1-9:  '))-1)
            (a,b) = (x//3,x%3)
            if (a,b) in actions:
                return (a,b)

    def reward(self,rewardValue):
        pass

    def resetStatesHistory(self):
        pass

class random_strategy():

    def SelectMove(self,board,actions,player_value):
        integer = random.randint(0,len(actions)-1)
        return actions[integer]

    def reward(self,value):
        pass

    def update(self, state_history,reward):
        pass


class q_strategy():
    def __init__(self, lr=0.5, discount=0.5,exploration=0.2,table=defaultdict(lambda: 0.0)):
        self.exploration = exploration
        self.lr = lr
        self.discount = discount
        self.values = table

    def update(self, state_history, reward):
        j=1
        for board in state_history:
            state = board.get_state()
            value1 = self.values[state]
            if j!= (len(state_history) -1):
                next_board = state_history[j]
                j += 1
                state2 = next_board.get_state()
                value2 = self.values[state2]
                #if value2 !=0: ic(value2)
            else:
                value2=reward
            value1 = (1-self.lr)*value1 + self.lr*(reward + value2*self.discount)
          
            self.values[state] = value1
        self.exploration *=0.9999

    #this bit is fine
    def SelectMove(self, board,actions,player_value):
        probability = random.uniform(0,1)
        #Should the model explore or stick to what it knows?
        if probability <= self.exploration:
            bestMove = actions[random.randint(0, len(actions)-1)]
        else:
            MaxValue = float('-inf')
            bestMove = actions[0]
            for (i,j) in actions:
                state2 = copy.deepcopy(board.get_state_list())
                state2[i][j] = player_value
                q_value = self.values.get(str(state2),0)
                if q_value > MaxValue:
                    MaxValue = q_value
                    bestMove = (i,j)
        return bestMove

    def save_table(self):
        return dict(self.values)

        
