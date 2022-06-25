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
                bets_holder[str(player)] = randint(self.min_bet, self.max_bet)
                print('stávka(€):', bets_holder[str(player)])

            else:
                while 1:
                    try:
                        print(f'{player}. hráč(TY)')
                        bets_holder[str(player)] = int(input('stávka(€): '))
                        
                        if bets_holder[str(player)] <= self.max_bet and bets_holder[str(player)] >= self.min_bet:
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
hands_holder = {
    '1' : [11,9],
    '2' : [11,3],
    '3' : [11,10],
    '4' : [11,10,9],
    'dealer' : [10,10,9]
}

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
    def __init__(self, n_of_players, user_order, max_value):
        super().__init__(n_of_players, user_order)
        self.max_value = max_value

    def playing(self):
        while True:
            self.sum_of_hand = sum(hands_holder[str(player)])
            for i, n in enumerate(hands_holder[f'{player}']):
                if self.sum_of_hand > self.max_value and n == 11:
                    hands_holder[f'{player}'][i] = 1
                    self.sum_of_hand = sum(hands_holder[str(player)])    

            if self.sum_of_hand>=21:
                return False

            if player != self.user_order:
                player_choice = randint(0,1)        
            
            else:
                print()
                print('TVOJE KARTY:', ', '.join(map(str,hands_holder[str(player)])))
                try:
                    player_choice = int(input('Ďalšia karta? 0=NIE/1=ANO: '))  

                except Exception as e:
                    print(e)
                    continue

            if player_choice == 0:
                return False
            
            hands_holder[f'{player}'].append(deck_of_cards.pop())

    @staticmethod  
    def print_hands():
        print(f'{player}.hráč:', end=' ')
        print(', '.join(map(str,hands_holder[str(player)])))

    def dealer_playing(self, d_min_value):
        self.d_min_value = d_min_value
        self.sum_of_hand = sum(hands_holder['dealer'])

        while True:
            self.sum_of_hand = sum(hands_holder['dealer'])

            for i, n in enumerate(hands_holder['dealer']):
                if self.sum_of_hand > self.max_value and n == 11:
                    hands_holder['dealer'][i] = 1
                    self.sum_of_hand = sum(hands_holder['dealer'])   
            
            if self.sum_of_hand > self.d_min_value-1:
                return False
            
            hands_holder['dealer'].append(deck_of_cards.pop())
    
    @staticmethod
    def print_dealer():
        print(f'dealer:', end=' ')
        print(', '.join(map(str,hands_holder['dealer'])))

game = Game(bets.n_of_players, bets.user_order, 21)
print('ŤAHANIE KARIET')
print('-------')
for player in range(1,game.n_of_players+1):
    game.playing()
    game.print_hands()

game.dealer_playing(17)
game.print_dealer()
print('-------')

class Results(Game):
    def __init__(self, n_of_players, user_order, max_value):
        super().__init__(n_of_players, user_order, max_value)

    def comparison(self):
        if sum(hands_holder['dealer']) <= self.max_value:
            if sum(hands_holder[str(player)]) >= sum(hands_holder['dealer']) and sum(hands_holder[str(player)]) <= self.max_value:
                if sum(hands_holder[str(player)]) == self.max_value and len(hands_holder[str(player)])==2 and len(hands_holder['dealer']) > 2:
                    print(f'{player}. hráč vyhral:', 1.5*bets_holder[str(player)])
                elif sum(hands_holder[str(player)]) > sum(hands_holder['dealer']):
                    print(f'{player}. hráč vyhral:', bets_holder[str(player)])
                elif sum(hands_holder[str(player)]) == sum(hands_holder['dealer']):
                    print(f'{player}. Remíza(Peniaze nevyhráva ani jeden)')    
        
            elif (sum(hands_holder[str(player)]) < sum(hands_holder['dealer'])) or (sum(hands_holder[str(player)]) > self.max_value):
                print(f'{player}. Dealer vyhral:', bets_holder[str(player)])
            
        

        else:
            if sum(hands_holder[str(player)]) > self.max_value:
                print(f'{player}. Dealer vyhral:', bets_holder[str(player)])
            
            elif sum(hands_holder[str(player)]) == self.max_value and len(hands_holder[str(player)])==2:
                print(f'{player}. hráč vyhral:', 1.5*bets_holder[str(player)])
            
            else:
                print(f'{player}. hráč vyhral:', bets_holder[str(player)])
    
results = Results(game.n_of_players, game.user_order, game.max_value)
print('VÝSLEDKY')
print('-------')
for player in range(1,results.n_of_players+1):
    results.comparison()

print(bets_holder)
print('-------')






