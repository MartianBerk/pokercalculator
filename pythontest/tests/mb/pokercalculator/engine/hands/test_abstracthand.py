from unittest import TestCase, main
from unittest.mock import Mock

from mb.pokercalculator.engine.hands.abstracthand import AbstractHand
from mb.pokercalculator.engine.model.card import Card


class MockImplementation(AbstractHand):
    pass


class AbstractHandTests(TestCase):
    def setUp(self):
        self.mock_card_deck = Mock()
        self.mock_self = MockImplementation(self.mock_card_deck)

    def test_probability(self):
        self.mock_card_deck.count.return_value = 46

        mock_outs = [Mock(spec=Card) for _ in range(0, 9)]

        result = AbstractHand.probability_from_outs(self.mock_self, mock_outs)
        self.assertEqual(result, 0.2)

    def test_probability_from_outs_simple(self):
        mock_outs = [Mock(spec=Card) for _ in range(0, 9)]

        with self.assertRaisesRegex(ValueError, "invalid betting_round, use 'flop' or 'turn'"):
            AbstractHand.probability_from_outs_simple(self.mock_self, mock_outs, "mock")

        # test flop
        result = AbstractHand.probability_from_outs_simple(self.mock_self, mock_outs, "flop")
        self.assertEqual(result, 0.36)

        # test turn
        result = AbstractHand.probability_from_outs_simple(self.mock_self, mock_outs, "turn")
        self.assertEqual(result, 0.18)


if __name__ == '__main__':
    main()
