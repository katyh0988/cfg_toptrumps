#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:10:51 2022

@author: katyhedgethorne
"""

import pandas as pd
import random

url = "https://raw.githubusercontent.com/APStats/Top-Trumps-data/master/Top" \
      "%20Trumps%20-%20Harry%20Potter%20and%20the%20Deathly%20Hallows%20Part" \
      "%202.csv"

cards_df = pd.read_csv(url)
cards_dict = cards_df.to_dict('index')

def deal():
    player = random.randint(0,29)
    opponent = random.randint(0,29)
    while player == opponent:
        opponent = random.randint(0,29)
    return [player, opponent]

def turn():
    p1_name = input("Player 1 name: \n")
    p2_name = input("Player 2 name: \n")
    cards = deal()
    player1 = cards[0]
    player2 = cards[1]
    print("\n{} draws {}".format(p1_name, list(cards_dict[player1].values())[0]))
    for n in range(1,6):
        print(list(cards_dict[player1].keys())[n] + ": " + \
              str(list(cards_dict[player1].values())[n]))
    skill = input("Pick a skill. Magic, cunning, courage, " \
                 "wisdom or temper?\n").capitalize()
    while skill not in cards_dict[0].keys():
        print("Skill not recognised.")
        skill = input("Choose magic, cunning, courage, wisdom or temper:\n").capitalize()
    print("\n{} draws {} with a {} score of {}\n".format(p2_name, cards_dict[player2]["Individual"], skill.upper(),str(cards_dict[player2][skill])))
   
    player1_score = cards_dict[player1][skill]
    player2_score = cards_dict[player2][skill]
   
    if player1_score > player2_score:
        print("{} wins!".format(p1_name))
    elif player1_score < player2_score:
        print("{} wins!".format(p2_name))
    else:
        print("It's a draw!") 
        


