from mb.pokercalculator.engine.calculator import Calculator
from mb.pokercalculator.engine.carddeck import CardDeck
from mb.pokercalculator.engine.model.card import Card
from mb.pokercalculator.engine.model.player import Player
from mylib.webapi import request, response, route


@route("/calculate", methods=["POST"])
def calculate():
    body = request.json

    try:
        players = body["players"]
        table = body["table"]

        card_deck = CardDeck()

        table_cards = [Card(c["suit"], c["value"]) for c in table["cards"]]
        for card in table_cards:
            card_deck.remove_card(card)

        playing = []
        hand = None
        outs = []
        cards = []
        for player in players:
            playing.append(Player())

            if player.get("visible"):
                try:
                    hand = player["hand"]
                    outs = [Card(o["suit"], o["value"]) for o in player["outs"]]
                    cards = [Card(c["suit"], c["value"]) for c in player["cards"]]
                except KeyError as e:
                    raise KeyError(f"player['{e}']")

        for card in cards:
            card_deck.remove_card(card)

        calculator = Calculator(players, card_deck)
        odds = calculator.calculate_from_outs(hand, outs)

        return response({"odds": odds})

    except KeyError as e:
        return {"error": f"missing {e} in body"}
