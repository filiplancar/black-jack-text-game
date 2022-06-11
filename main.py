from abc import ABC, abstractmethod
from random import randint

class Players(ABC):
    @abstractmethod
    def __init__(self, n_of_players, user_order):
        self.n_of_players = n_of_players
        self.user_order = user_order

class Bets(Players):
    def __init__(self, n_of_players, user_order, min_bet, max_bet):
        super().__init__(n_of_players, user_order)  
        self.min_bet = min_bet
        self.max_bet = max_bet
        
    
    def betting(self):
        bets_holder = {}
        for player in range(1,self.n_of_players+1):
            if player != self.user_order:    
                print(f'{player}. hráč')
                bets_holder['player_' + str(player)] = randint(self.min_bet, self.max_bet)
                print('stávka(€):', bets_holder['player_' + str(player)])

            else:
                while 1:
                    try:
                        print(f'{player}. hráč')
                        bets_holder['player_' + str(player)] = int(input('stávka(€): '))
                        
                        if bets_holder['player_' + str(player)] <= self.max_bet and bets_holder['player_' + str(player)] >= self.min_bet:
                            break

                    except ValueError as e:
                        print('Zle zvolená stávka')
                        continue

bets = Bets(4, randint(1, 4), 1000, 10000)
print('STÁVKY')
print(f'min. stávka: {bets.min_bet}, ' + f'max. stávka: {bets.max_bet}')
print('-------')
bets.betting()
print('-------')



