from unittest import TestCase, main
from unittest.mock import Mock, patch

from mb.pokercalculator.engine.hands.handfactory import HandFactory


class HandFactoryTests(TestCase):
    @patch("mb.pokercalculator.engine.hands.handfactory.RoyalFlush")
    def test_get(self, mock_royal_flush):
        mock_card_deck = Mock()

        # test one - error
        with self.assertRaisesRegex(ValueError, "mock is an unknown hand"):
            HandFactory.get("mock", mock_card_deck)

        # test two - Royal Flush
        hand = HandFactory.get("royalflush", mock_card_deck)
        mock_royal_flush.assert_called_with(mock_card_deck)
        self.assertEqual(hand, mock_royal_flush.return_value)


if __name__ == '__main__':
    main()
