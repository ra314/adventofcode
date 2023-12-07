import numpy as np
from collections import defaultdict
from collections import Counter
import itertools
import re
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

FIVE_OF_A_KIND = 10
FOUR_OF_A_KIND = 9
FULL_HOUSE = 8
THREE_OF_A_KIND = 7
TWO_PAIR = 6
ONE_PAIR = 5
HIGH_CARD = 4

card_chars = "AKQT98765432J"
non_jokers = card_chars[:-1]
card_lexes = "ABCDEFGHIJKLM"[::-1]
mapping = dict(map(lambda i,j : (i,j) , card_chars,card_lexes))

def replace_recurse(hand):
  if not "J" in hand:
    return [hand]
  index = hand.find("J")
  new_hands = []
  for non_joker in non_jokers:
    new_hands.append(hand[:index] + non_joker + hand[index+1:])
  return list(itertools.chain.from_iterable(list(map(replace_recurse, new_hands))))
  

def score_hand_plus_tiebreak(hand):
  best_score = max([score_hand(new_hand) for new_hand in replace_recurse(hand)])
  tiebreak = "".join([mapping[char] for char in hand])
  return best_score + tiebreak

def score_hand(hand):
  counts = Counter(list(hand))
  values = sorted(list(counts.values()), reverse=True)
  if values[0] == 5:
    return chr(ord("A")+FIVE_OF_A_KIND)
  if values[0] == 4:
    return chr(ord("A")+FOUR_OF_A_KIND)
  if values[0] == 3 and values[1] == 2:
    return chr(ord("A")+FULL_HOUSE)
  if values[0] == 3:
    return chr(ord("A")+THREE_OF_A_KIND)
  if values[0] == 2 and values[1]==2:
    return chr(ord("A")+TWO_PAIR)
  if values[0] == 2:
    return chr(ord("A")+ONE_PAIR)
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

