let score = 0;

let last_card_value = 0;

function update_score() {
    document.getElementById("score").innerHTML = score;
}

function checkBigger() {

    let response = newCard()

    let value = parseInt(response["value"]);

    if (last_card_value < value) {
        score += 1;

        console.log("SCORE");
        console.log(score);
    }

    startGame(response);
    update_score()
}

function checkLess() {

    let response = newCard();

    let value = parseInt(response["value"]);

    if (last_card_value > value) {
        score += 1;
        console.log("SCORE");
        console.log(score);
    }

    startGame(response);

    update_score();
}

function startGame(response = null) {
    response = null ? response : newCard();

    console.log(response["image"]);

    document.getElementById("img").src = response["image"];

    last_card_value = response["value"];

    document.getElementById("value").innerHTML = last_card_value;

    document.getElementById("title").innerHTML = response["suit"];

    document.getElementById("btn").style.display = "none";

    document.getElementById("btn-2").style.display = "block";
}

function newCard() {
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "/new_card_json", false);

    xhttp.send();

    let response = JSON.parse(xhttp.responseText);

    return response;
}