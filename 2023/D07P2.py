import numpy as np
from collections import defaultdict
from collections import Counter
import re
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()

FIVE_OF_A_KIND = 10
FOUR_OF_A_KIND = 9
FULL_HOUSE = 8
THREE_OF_A_KIND = 7
TWO_PAIR = 6
ONE_PAIR = 5
HIGH_CARD = 4

card_chars = "AKQT98765432J"
card_lexes = "ABCDEFGHIJKLM"[::-1]
mapping = dict(map(lambda i,j : (i,j) , card_chars,card_lexes))

def score_hand_plus_tiebreak(hand):
  score = score_hand(hand)
  tiebreak = "".join([mapping[char] for char in hand])
  return score + tiebreak

def score_hand(hand):
  num_jokers = hand.count("J")
  if num_jokers >= 4:
    return chr(ord("A")+FIVE_OF_A_KIND)
  print(hand)
  counts = Counter(list(hand))
  if "J" in counts:
    del counts["J"]
  values = sorted(list(counts.values()), reverse=True)
  if values[0] == 5:
    return chr(ord("A")+FIVE_OF_A_KIND)
  if values[0] == 4:
    if num_jokers > 1:
      return chr(ord("A")+FIVE_OF_A_KIND)
    return chr(ord("A")+FOUR_OF_A_KIND)
  if values[0] == 3 and len(values)>1 and values[1] == 2:
    if num_jokers == 1:
      return chr(ord("A")+FOUR_OF_A_KIND)
    elif num_jokers >= 2:
      return chr(ord("A")+FIVE_OF_A_KIND) 
    return chr(ord("A")+FULL_HOUSE)
  if values[0] == 3:
    if num_jokers == 1:
      return chr(ord("A")+FOUR_OF_A_KIND)
    elif num_jokers >= 2:
      return chr(ord("A")+FIVE_OF_A_KIND) 
    return chr(ord("A")+THREE_OF_A_KIND)
  if values[0] == 2 and len(values)>1 and values[1]==2:
    if num_jokers == 1:
      return chr(ord("A")+FULL_HOUSE)
    elif num_jokers == 2:
      return chr(ord("A")+FOUR_OF_A_KIND) 
    elif num_jokers == 3:
      assert(False)
    return chr(ord("A")+TWO_PAIR)
  if values[0] == 2:
    if num_jokers == 1:
      return chr(ord("A")+THREE_OF_A_KIND)
    elif num_jokers == 2:
      return chr(ord("A")+FOUR_OF_A_KIND)
    elif num_jokers == 3:
      return chr(ord("A")+FIVE_OF_A_KIND) 
    return chr(ord("A")+ONE_PAIR)
  if num_jokers == 1:
    if num_jokers == 1:
      return chr(ord("A")+ONE_PAIR)
    elif num_jokers == 2:
      return chr(ord("A")+THREE_OF_A_KIND)
    elif num_jokers == 3:
      assert(False)
  return chr(ord("A")+HIGH_CARD) 

hands_and_bids = []
for line in content.splitlines():
  hand, bid = line.split()
  bid = int(bid)
  hands_and_bids.append([hand, bid])

sorted_hands_and_bids = sorted(hands_and_bids, key=lambda x: score_hand_plus_tiebreak(x[0]))

winnings = 0
for i, hand_and_bid in enumerate(sorted_hands_and_bids):
  bid = hand_and_bid[1]
  curr_winnings = (i+1) * bid
  print(curr_winnings)
  winnings += curr_winnings

print(winnings)

