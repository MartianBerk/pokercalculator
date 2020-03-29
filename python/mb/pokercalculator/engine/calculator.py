from .carddeck import CardDeck
from .hands.abstracthand import AbstractHand


class Calculator:
    def __init__(self, players, card_deck):
        """Calculate best odds with whats on the table.

        Args:
            players (list): List of Player objects.
            card_deck (CardDeck): CardDeck object.
        """
        self._players = players
        self._card_deck = card_deck

    def calculate_from_outs(self, target_hand, outs, betting_round):
        """Given a target Hand and a list of Cards which are the 'outs', calculate odds.

        Args:
            target_hand (AbstractHand): Target Hand.
            outs (list): List of Card objects.
            betting_round (str): Betting round ('flop' or 'turn').

        Returns:
            float: Odds of success.
        """
        hand = target_hand(self._card_deck)
        return hand.probability_from_outs(outs, betting_round)
