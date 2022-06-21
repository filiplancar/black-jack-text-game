from abc import ABC, abstractmethod
from random import randint, shuffle

print('-------')
print('BLACK JACK')
print('-------')
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
print('STÁVKY')
print(f'min. stávka: {bets.min_bet}, ' + f'max. stávka: {bets.max_bet}')
print('-------')
bets.betting()
print('-------')

deck_of_cards = 4*[2,3,4,5,6,7,8,9,10,10,10,10,11]
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
            hands_holder[str(player)] = temp
    
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

class Game(Players):
    def __init__(self, n_of_players, user_order, max_value, d_min_value):
        super().__init__(n_of_players, user_order)
        self.max_value = max_value
        self.d_min_value = d_min_value

    def playing(self):
        self.sum_of_hand = sum(hands_holder[str(player)]) 
        player_choice = 1

        while True:
            for i, n in enumerate(hands_holder[f'{player}']):
                if self.sum_of_hand > self.max_value and n == 11:
                    hands_holder[f'{player}'][i] = 1
                    self.sum_of_hand = sum(hands_holder[str(player)])    

            player_choice = randint(0,1)        
            if (self.sum_of_hand>=21) or (player_choice == 0):
                return False
            
            hands_holder[f'{player}'].append(deck_of_cards.pop())
            self.sum_of_hand = sum(hands_holder[str(player)])
            
    
    def print_hands(self):
        print(f'{player}.hráč:', end=' ')
        print(', '.join(map(str,hands_holder[str(player)])))
            
game = Game(bets.n_of_players, bets.user_order, 21, 17)
print('ŤAHANIE KARIET')
print('-------')
for player in range(1,game.n_of_players+1):
    game.playing()
    game.print_hands()

print('-------')








