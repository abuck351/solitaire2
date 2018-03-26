from card import Card


class Pile:
    def __init__(self, pile_type: str, cards: [Card] = [], number: int = None):
        self.type = pile_type
        self.number = number
        self.cards = cards

    def update_card_positions(self) -> None:
        '''
        Updates all the positions of the cards in the pile
        to match the pile_number and position in pile
        '''
        for index, card in enumerate(self):
            card.position = (self.number, index)

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)
