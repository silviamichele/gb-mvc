from flask import render_template


def render_card_template(response_card):
    return render_template("hello.html",
                           card_url=response_card["image"],
                           card_value=response_card["value"],
                           card_name=response_card["suit"])
