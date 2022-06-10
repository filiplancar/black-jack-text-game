from abc import ABC, abstractmethod
import random

class Players(ABC):
    @abstractmethod
    def __init__(self, number_of_players, player_user_order):
        self.n_of_players = number_of_players
        self.p_user_order = player_user_order

class Bets(Players):
    def __init__(self, number_of_players, player_user_order):
        super().__init__(number_of_players, player_user_order)  

# players = Players(4, random.choice(range(1, 4)))



