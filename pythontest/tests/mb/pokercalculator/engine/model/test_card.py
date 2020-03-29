from unittest import TestCase, main

from mb.pokercalculator.engine.model.card import Card


class CardTests(TestCase):
    def test_init(self):
        expected_suits = ["club", "diamond", "heart", "spade"]
        expected_values = [str(v) for v in range(2, 11)] + ["J", "Q", "K", "A"]

        with self.assertRaisesRegex(TypeError, f"expected suit to be {str}"):
            Card(123, "value")

        with self.assertRaisesRegex(ValueError, f"expected suit to be one of {', '.join(expected_suits)}"):
            Card("suit", "value")

        with self.assertRaisesRegex(TypeError, f"expected value to be {str}"):
            Card("spade", 123)

        with self.assertRaisesRegex(ValueError, f"expected value to be one of {', '.join(expected_values)}"):
            Card("spade", "value")

        card = Card("spade", "a")
        self.assertEqual(card.suit, "spade")
        self.assertEqual(card.value, "A")


if __name__ == '__main__':
    main()
