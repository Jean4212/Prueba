var buttonUp = () => {
    const input = document.querySelector(".searchbox-input");
    const cards = document.getElementsByClassName("col");
    let filter = input.value
    for (let i = 0; i < cards.length; i++) {
        let title = cards[i].querySelector(".card-body");
        if (title.innerText.toUpperCase().indexOf(filter.toUpperCase()) > -1) {
            cards[i].classList.remove("d-none")
        } else {
            cards[i].classList.add("d-none")
        }
    }
}

document.getElementById("search").addEventListener("search", function(event) {
    const input = document.querySelector(".searchbox-input");
    const cards = document.getElementsByClassName("col");
    let filter = input.value
    for (let i = 0; i < cards.length; i++) {        
        cards[i].classList.remove("d-none")
        }
    }
  );
