from abc import ABC, abstractmethod
from random import randint, shuffle
class Players(ABC):
    @abstractmethod
    def __init__(self, n_of_players, user_order):
        self.n_of_players = n_of_players
        self.user_order = user_order

bets_holder = {}
class Bets(Players):
    def __init__(self, n_of_players, user_order, min_bet, max_bet):
        super().__init__(n_of_players, user_order)  
        self.min_bet = min_bet
        self.max_bet = max_bet
        
    def betting(self):
        for player in range(1,self.n_of_players+1):
            if player != self.user_order:    
                print(f'{player}. hráč')
                bets_holder['player_' + str(player)] = randint(self.min_bet, self.max_bet)
                print('stávka(€):', bets_holder['player_' + str(player)])

            else:
                while 1:
                    try:
                        print(f'{player}. hráč(TY)')
                        bets_holder['player_' + str(player)] = int(input('stávka(€): '))
                        
                        if bets_holder['player_' + str(player)] <= self.max_bet and bets_holder['player_' + str(player)] >= self.min_bet:
                            break

                    except ValueError as e:
                        print('Zle zvolená stávka')
                        continue

bets = Bets(4, randint(1, 4), 1000, 10000)
# print('STÁVKY')
# print(f'min. stávka: {bets.min_bet}, ' + f'max. stávka: {bets.max_bet}')
# print('-------')
# bets.betting()
# print('-------')

deck_of_cards = 4*[1,2,3,4,5,6,7,8,9,10,10,10,10]
hands_holder = {}
class Dealing(Players):
    def __init__(self, n_of_players, hand, user_order='None'):
        super().__init__(n_of_players, user_order)    
        self.hand = hand
    
    @staticmethod
    def shuffle_cards():
        shuffle(deck_of_cards)

    def players_hand(self):
        for player in range(1,self.n_of_players+1):
            temp = []
            for card in range(1, self.hand+1):
                temp.append(deck_of_cards.pop())
                
            print(f'{player}.hráč: ' + ', '.join(map(str, temp))) 
            hands_holder['player_' + str(player)] = temp
            # print(', '.join(hands_holder['player_' + str(player)]))
    
    def dealers_hand(self):
        temp = []
        for card in range(1, self.hand+1):
            temp.append(deck_of_cards.pop())
        
        print(f'dealer: {temp[0]}, ?')
        hands_holder['dealer'] = temp
    
                
dealing = Dealing(bets.n_of_players, 2)
print('DEALOVANIE')
print('-------')
dealing.shuffle_cards()
dealing.players_hand()
dealing.dealers_hand()
print('-------')








