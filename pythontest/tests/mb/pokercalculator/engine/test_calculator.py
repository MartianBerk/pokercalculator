from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.pokercalculator.engine.calculator import Calculator


class CalculatorTests(TestCase):
    def setUp(self):
        self.mock_card_deck = Mock()
        self.mock_players = Mock
        self.mock_self = Mock(_card_deck=self.mock_card_deck,
                              _players=self.mock_players)

    def test_init(self):
        calculator = Calculator(self.mock_players, self.mock_card_deck)
        self.assertEqual(calculator._card_deck, self.mock_card_deck)
        self.assertEqual(calculator._players, self.mock_players)

    @patch("mb.pokercalculator.engine.calculator.HandFactory.get")
    def test_calculate_from_outs(self, mock_hand_factory):
        mock_hand_factory.return_value.probability_from_outs.return_value = 0.1

        mock_hand = "mock_hand"
        mock_outs = [Mock()]

        result = Calculator.calculate_from_outs(self.mock_self, mock_hand, mock_outs)
        mock_hand_factory.assert_called_with("mock_hand", self.mock_card_deck)
        mock_hand_factory.return_value.probability_from_outs.assert_called_with(mock_outs)
        self.assertEqual(result, 0.1)


if __name__ == '__main__':
    main()
