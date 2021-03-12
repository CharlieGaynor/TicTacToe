import main
from collections import defaultdict
from board import board
from game import game
from player import player
from strategies import random_strategy, q_strategy,Human
from collections import defaultdict
import pickle
import json
from human_game import HumanGame
import copy


while True:
    game_mode = input('What game mode do you want to play? Pick from:\n 1. Human vs AI, 2. AI vs Human, 3. Human vs Human [type a number 1, 2 or 3]')

    try:
        game_mode = int(game_mode)
    except:
        print("\nThat wasn't valid, please try again!\n")
    if game_mode not in [1,2,3]:
        print("\nThat wasn't valid, please try again!\n")

    if game_mode == 1:
        main.HumanVSAI()

    if game_mode == 2:
        main.AIVSHuman()

    if game_mode == 3:
        main.HumanVSHuman()

    play_again = input('Do you want to play again? Y or N ')

    if play_again.lower() == 'n':
        break
