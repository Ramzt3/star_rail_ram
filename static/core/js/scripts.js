function myFunction() {
  	const input = document.getElementById("myInput").value.toUpperCase();
	const cardContainer = document.getElementById("card-list")
	// console.log(cardContainer);

	const cards = cardContainer.getElementsByClassName("card");
	// console.log(cards);

	for(let i = 0; i < cards.length; i++) {
		let title = cards[i].querySelector(".card-body h3.card-title")
		// console.log(title);

		if(title.innerText.toUpperCase().indexOf(input) > -1) {
			cards[i].style.display = "";
		} else {
			cards[i].style.display = "none";
		}
	}
}


function multiCheckbox() {
	const form = document.getElementById("filter-form");
	console.log(form);
}


// Used to toggle the menu on small screens when clicking on the menu button
function mbNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
