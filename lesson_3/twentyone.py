'''
assignment : 21
52 card deck, 4 suits, 13 vals(2,3,4,5,6,7,8,9,10, j,q,k,a)
dont go over 21 or yo ulose

2-10: face value, j/q/k:10, a: 1 or 11

player hits until stay or bust
dealer hits until 17+
see who has closest to 21


'''


def initiate_deck():
  value = [i for i in range(1,14)]
  face = ['clubs', 'diamond' , 'heart', 'spade']
  print(face, value)

def play_game():
  deck = initiate_deck()

play_game() 