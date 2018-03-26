BLACK = 0
RED = 1
SUITS = ('diamonds', 'hearts', 'spades', 'clubs')
RANKS = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')


class Card:
    def __init__(self, suit: str, rank: str, face_up=False):
        assert suit in SUITS, f'suit {suit} does not exist'
        assert rank in RANKS, f'rank {rank} does not exist'

        self.suit = suit
        self.rank = rank
        self.face_up = face_up
        self.position = None

    @property
    def image_filename(self) -> str:
        '''
        Returns the name of the png image that should be used
        '''
        return f'{self.rank}_of_{self.suit}.png'

    @property
    def color(self) -> int:
        '''
        Returns BLACK if the card is spades or clubs and
        returns RED if the card is diamonds or hearts
        '''
        return BLACK if self.suit == 'spades' or self.suit == 'clubs' else RED

    def __str__(self):
        return f'{self.rank.capitalize()} of {self.suit.capitalize()}'

    def __repr__(self):
        return f'Card({self.position}, {self.suit}, {self.rank}, face_up={self.face_up})'
