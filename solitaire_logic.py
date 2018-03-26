import random
import colors
from card import Card
from pile import Pile

SUITS = ('diamonds', 'hearts', 'spades', 'clubs')
RANKS = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')


class GameState:
    def __init__(self, piles: [Pile] = []):
        if piles == []:
            self.piles = self._init_piles()
        else:
            self.piles = piles

        self._update_all_card_positions()

    def _init_piles(self) -> [Pile]:
        '''
        Initializes a new list of piles randomly. Used 
        when starting a new game
        '''
        cards = self._generate_random_deck()
        piles = [] 

        piles.append(Pile('tableau', [cards[0]], number=0))
        piles.append(Pile('tableau', cards[1:3], number=1))
        piles.append(Pile('tableau', cards[3:6], number=2))
        piles.append(Pile('tableau', cards[6:10], number=3))
        piles.append(Pile('tableau', cards[10:15], number=4))
        piles.append(Pile('tableau', cards[15:21], number=5))
        piles.append(Pile('tableau', cards[21:28], number=6))

        piles.append(Pile('stock', cards[28:]))
        piles.append(Pile('waste'))

        piles.append(Pile('foundation', number=0))
        piles.append(Pile('foundation', number=1))
        piles.append(Pile('foundation', number=2))
        piles.append(Pile('foundation', number=3))

        return piles

    def _update_all_card_positions(self) -> None:
        '''
        Loops through every card in every pile in order to update its position
        '''
        for pile in self.piles:
            pile.update_card_positions()

    @property
    def tableaus(self) -> [Pile]:
        '''
        Just the tableaus, not the stock, waste, nor foundation
        '''
        return self.piles[:7]

    def _generate_random_deck(self) -> [Card]:
        '''
        Generates a list of Card objects in a random order
        ''' 
        cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        random.shuffle(cards)
        return cards

    def _largest_tableau(self) -> Pile:
        '''
        Returns the tableau with the longest length
        '''
        longest = self.tableaus[0]
        for tableau in self.tableaus[1:]:
            if len(tableau) > len(longest):
                longest = tableau
        return longest

    def __str__(self):
        widths = [max([len(str(card)) for card in tableau]) for tableau in self.tableaus]
        separator = '   '
        game_state_output = []

        for row in range(len(self._largest_tableau())):
            for col in range(len(self.tableaus)):
                try:
                    width_difference = (widths[col] - len(str(self.tableaus[col][row])))
                    game_state_output.append(str(self.tableaus[col][row]) + (' ' * width_difference) + separator)
                except IndexError:
                    game_state_output.append((' ' * (widths[col])) + separator)
            game_state_output.append('\n')

        return ''.join(game_state_output)
