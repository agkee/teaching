const form = document.getElementById("form");

let requestUrl = "https://nba-players.herokuapp.com/";

form.addEventListener("submit", (e) => {
  e.preventDefault();
  //   getPlayerImage("Lebron", "James");

  getPlayerImage("James", "Harden");
});

async function getPlayerImage(firstName, lastName) {
  console.log("Pokemon info is called");
  let endpointURL = requestUrl + "players/" + lastName + "/" + firstName;
  const res = await fetch(endpointURL); //GET request
  const data = await res.blob();
  const imgURL = URL.createObjectURL(data);
  document.querySelector("img").src = imgURL;
}
