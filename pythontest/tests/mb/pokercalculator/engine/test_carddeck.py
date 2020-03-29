from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.pokercalculator.engine.carddeck import CardDeck
from mb.pokercalculator.engine.model.card import Card


class CardDeckTests(TestCase):
    def setUp(self):
        self.mock_ace_spade = Mock(spec=Card)
        self.mock_two_diamonds = Mock(spec=Card)
        self.mock_king_hearts = Mock(spec=Card)

        self.mock_self = Mock(_cards=[self.mock_ace_spade,
                                      self.mock_two_diamonds,
                                      self.mock_king_hearts])

    @patch("mb.pokercalculator.engine.carddeck.Card")
    def test_init(self, mock_card):
        CardDeck()
        self.assertEqual(mock_card.call_count, 52)  # 52 cards in a deck

    def test_iter(self):
        cards = [c for c in CardDeck.__iter__(self.mock_self)]
        self.assertEqual(cards[0], self.mock_ace_spade)
        self.assertEqual(cards[1], self.mock_two_diamonds)
        self.assertEqual(cards[2], self.mock_king_hearts)

    def test_remove_card(self):
        # not found
        mock_card = Mock(spec=Card)
        self.assertEqual(len(self.mock_self._cards), 3)
        CardDeck.remove_card(self.mock_self, mock_card)
        self.assertEqual(len(self.mock_self._cards), 3)

        # found
        CardDeck.remove_card(self.mock_self, self.mock_ace_spade)
        self.assertEqual(len(self.mock_self._cards), 2)

    def test_count(self):
        self.assertEqual(CardDeck.count(self.mock_self), 3)


if __name__ == '__main__':
    main()
