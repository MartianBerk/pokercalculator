from abc import ABCMeta, abstractmethod


class AbstractHand(metaclass=ABCMeta):
    def __init__(self, card_deck):
        """Blueprint for poker hands.

        Args:
            card_deck (CardDeck): CardDeck object.
        """
        self._card_deck = card_deck

    def probability_from_outs(self, outs):
        """Calculate the probability of winning given a list of 'outs'.

        Args:
            outs (list): List of Card objects.

        Returns:
            float: Probability of winning.
        """
        # return round(len(outs) / (self._card_deck.count() - len(outs)), 2)
        outs = len(outs)
        remaining_cards = self._card_deck.count() - outs
        return round(1 / ((remaining_cards / outs) + 1), 2)

    def probability_from_outs_simple(self, outs, betting_round):
        """Calculate the probability of winning given a list of 'outs', using the simple approach (Rule of 4 and 2).

        Round can be either 'flop' (x4) or 'turn' (x2).

        Args:
            outs (list): List of Card objects.
            betting_round (str): Betting round ('flop' or 'turn').

        Returns:
            float: Probability of winning.
        """
        if betting_round == "flop":
            return round(len(outs) * 4 / 100, 2)
        elif betting_round == "turn":
            return round(len(outs) * 2 / 100, 2)

        raise ValueError("invalid betting_round, use 'flop' or 'turn'")
