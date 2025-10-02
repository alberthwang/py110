'''
assignment : 21
52 card deck, 4 suits, 13 vals(2,3,4,5,6,7,8,9,10, j,q,k,a)
dont go over 21 or yo ulose

2-10: face value, j/q/k:10, a: 1 or 11

player hits until stay or bust
dealer hits until 17+
see who has closest to 21


1. initilize deck
2. deal cards to play and human
3. player turn:hit or stay
4. if busts dealer wins
5. dealer turn: hit or stay
repeat until total >= 17
6. if dealer bust, player wins
7. compare cards and decide winner 
'''

import random

def shuffle(deck):
    random.shuffle(deck)
    

def initiate_deck():
  values = [i for i in range(1,14)]
  suits = ['clubs', 'diamond' , 'heart', 'spade']
  cards = [f"{suit}, {value}" for suit in suits for value in values]
  #print(cards)
  #deck = {i: [suits[(i- 1) // 13], (i % 13) + 1] for i in range(1,53)}
  deck = [[card] for card in cards]
  #print(deck)
  return deck
  
def draw_card(deck):
  return deck.pop()


def play_game():
  deck = initiate_deck()
  shuffle(deck)
  print(deck)
  print(draw_card(deck))

play_game() 