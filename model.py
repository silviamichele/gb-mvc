import requests


class Deck:
    def __init__(self, deck_id=None):
        self.deck_id = deck_id

    def shuffle_deck(self):
        response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/')
        data = response.json()
        self.deck_id = data['deck_id']

    def draw_card(self):
        response = requests.get(f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count=1')
        data = response.json()
        return data['cards'][0]
