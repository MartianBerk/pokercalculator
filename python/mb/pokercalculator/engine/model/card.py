class Card:
    _attrs = {
        "suit": {
            "type": str,
            "values": ["club", "diamond", "heart", "spade"]
        },
        "value": {
            "type": str,
            "values": [str(v) for v in range(2, 11)] + ["J", "Q", "K", "A"]
        }
    }

    def __init__(self, suit, value):
        f"""Card blueprint.
        
        Args:
            suit (str): Cards suit ({', '.join(self._attrs['suit']['values'])}). 
            value (str): Cards value ({', '.join(self._attrs['value']['values'])}). 
        """
        if not isinstance(suit, self._attrs["suit"]["type"]):
            raise TypeError(f"expected suit to be {self._attrs['suit']['type']}")

        suit = suit.lower()
        if suit not in self._attrs['suit']['values']:
            raise ValueError(f"expected suit to be one of {', '.join(self._attrs['suit']['values'])}")

        if not isinstance(value, self._attrs["value"]["type"]):
            raise TypeError(f"expected value to be {self._attrs['value']['type']}")

        value = value.upper()
        if value not in self._attrs['value']['values']:
            raise ValueError(f"expected value to be one of {', '.join(self._attrs['value']['values'])}")

        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value
