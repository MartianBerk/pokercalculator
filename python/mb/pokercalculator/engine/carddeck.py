from mb.pokercalculator.engine.model.card import Card


class CardDeck:
    def __init__(self):
        """Represents a standard 52 card deck."""
        suits = ["club", "diamond", "heart", "spade"]
        values = [str(v) for v in range(2, 11)] + ["J", "Q", "K", "A"]

        self._cards = [Card(s, v) for v in values for s in [s for s in suits]]

    def __iter__(self):
        """Iterate through the card deck.

        Returns:
            Iterable[Card]: Cards in the deck.
        """
        for c in self._cards:
            yield c

    def remove_card(self, card):
        """Remove card from deck.

        Args:
            card (Card): The card to remove.
        """
        try:
            self._cards.remove(card)
        except ValueError:
            pass  # card not in deck

    def count(self):
        """Count the number of cards in the deck."""
        return len(self._cards)
