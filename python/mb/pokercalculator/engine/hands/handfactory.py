from .royalflush import RoyalFlush


class HandFactory:
    @staticmethod
    def get(hand, card_deck):
        """Load a Hand object.

        Args:
            hand (str): Required hand.
            card_deck (CardDeck): CardDeck object to be used by the Hand.

        Returns:
            AbstractHand: The requested hand.
        """
        try:
            return {
                "royalflush": RoyalFlush
            }[hand](card_deck)
        except KeyError:
            raise ValueError(f"{hand} is an unknown hand")
