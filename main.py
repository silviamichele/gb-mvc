import flask
from model import Deck
from settings import settings
from view import render_card_template

APP = flask.Flask(__name__)

score_handler = {
    "JACK": 11,
    "ACE": 1,
    "KING": 13,
    "QUEEN": 12
}


@APP.route("/new_card")
def get_new_card():
    deck = Deck()

    if not settings.DECK_CODE:
        deck_id = deck.shuffle_deck()

        settings.DECK_CODE = deck_id

    else:
        deck.deck_id = settings.DECK_CODE

    new_card = deck.draw_card()

    if score := score_handler.get(new_card["value"]):
        new_card["value"] = score

    return render_card_template(new_card)


@APP.route("/new_card_json")
def get_new_card_json():
    deck = Deck()

    if not settings.DECK_CODE:
        deck_id = deck.shuffle_deck()

        settings.DECK_CODE = deck_id

    else:
        deck.deck_id = settings.DECK_CODE

    new_card = deck.draw_card()

    if score := score_handler.get(new_card["value"]):
        new_card["value"] = score

    return new_card


if __name__ == '__main__':
    APP.run(port=5000, threaded=True)
