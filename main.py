from board import board
from game import game
from player import player
from strategies import random_strategy, q_strategy,Human
#from q_strategy import q_strategy
from collections import defaultdict
import pickle
from icecream import ic
import json
from human_game import HumanGame

##############################################################
#Importing the tables from previous learning, to save computation
#You can retrain the agents if you like. These tables were generated
#after training for 2 million games. This is more than enough to 
#ensure the agent plays perfectly (either 1st or second)
with open('table_first.txt') as fobj:
        table1 = json.load(fobj)
with open('table_second.txt') as fobj:
        table2 = json.load(fobj)
###############################################################


def AIvsRandom(number_games,train=False):
    if train:
        player1 = player(1,q_strategy(lr=0.5,exploration=0.4,discount=0.8))
        player2 = player(-1,random_strategy())
        board1 = board()
        game1 = game(board1,player1,player2)
        game1.learn_many_games(number_games)
        print('---------------------','\nAI VS Random STATS (learning)')
        game1.print_stats()
        print('---------------------')
    else:
        player1 = player(1,q_strategy(lr=0,exploration=0,discount=0,table=table1))
        player2 = player(-1,random_strategy())
        board1 = board()
        game1 = game(board1,player1,player2)
        game1.play_many_games(number_games)
        print('---------------------','\nAI VS Random STATS')
        game1.print_stats()
        print('---------------------')

    #table_save = player1.strategy.save_table()
    #with open('table_first.txt', 'w') as fobj:
        #json.dump(table_save,fobj)


#AI goes second
def RandomVSAI(number_games,train=False):
    if train:
        player1 = player(1,random_strategy())
        player2 = player(-1,q_strategy(lr=0.5,exploration=0.4,discount=0.8))
        board1 = board()
        game1 = game(board1,player1,player2)
        game1.learn_many_games(number_games)
        print('---------------------','\nRandom VS AI STATS (learning)')
        game1.print_stats()
        print('---------------------')
    else:
        player1 = player(1,random_strategy())
        player2 = player(-1,q_strategy(lr=0,exploration=0,discount=0,table=table2))
        board1 = board()
        game1 = game(board1,player1,player2)
        game1.play_many_games(number_games)
        print('---------------------','\nRandom VS AI STATS')
        game1.print_stats()
        print('---------------------')

    #table_save = player2.strategy.save_table()
    #with open('table_second.txt', 'w') as fobj:
        #json.dump(table_save,fobj)

#######################################################################
#Vs human player, with a.i as player 1
#######################################################################

def AIVSHuman():
    

    player1 = player(1,q_strategy(lr=0,exploration=0,discount=0,table=table1))
    player2 = player(-1,Human())
    board1 = board()

    game1 = HumanGame(board1,player1,player2,human_value = -1)
    game1.play_many_games()


###########################################################################

#Vs human player, with a.i as player 1
#######################################################################
def HumanVSAI():

    

    player1 = player(1,Human())
    player2 = player(-1,q_strategy(lr=0,exploration=0,discount=0,table=table2))
    board2 = board()

    game2 = HumanGame(board2,player1,player2,human_value=1)
    game2.play_many_games()
######################################################################
#AI vs AI
######################################################################
def AIVSAI(number_games,train=False):
    if train:
        player1 = player(1,q_strategy(lr=0.5,exploration=0.4,discount=0.8))
        player2 = player(-1,q_strategy(lr=0.5,exploration=0.4,discount=0.8))
        board1 = board()
        game2 = game(board1,player1,player2)
        game2.learn_many_games(number_games)
        print('---------------------','\nAI VS AI STATS (learning)')
        game2.print_stats()
        print('---------------------')
    else:
        player1 = player(1,q_strategy(lr=0,exploration=0,discount=0,table=table1))
        player2 = player(-1,q_strategy(lr=0,exploration=0,discount=0,table=table2))
        board1 = board()
        game2 = game(board1,player1,player2)
        game2.play_many_games(number_games)
        print('---------------------','\nAI VS AI STATS')
        game2.print_stats()
        print('---------------------')

AIVSAI(10,train=False)
RandomVSAI(100)
AIvsRandom(100)