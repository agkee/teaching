// @ts-nocheck
const form = document.getElementById("form");

let requestUrl = "https://nba-players.herokuapp.com/";

form.addEventListener("submit", (e) => {
  e.preventDefault();
  //   getPlayerImage("Lebron", "James");

  getPlayerImage("James", "Harden");
});

async function getPlayerImage(firstName, lastName) {
  // console.log("Pokemon info is called");
  // let endpointURL = requestUrl + "players/" + lastName + "/" + firstName;
  // const res = await fetch(endpointURL); //GET request
  // const data = await res.blob();
  // const imgURL = URL.createObjectURL(data);
  // document.querySelector("img").src = imgURL;
  let endpointURL = "http://localhost:5000/test";
  const res = await fetch(endpointURL); //GET request
  const data = await res.text();
  console.log(data);
}

async function send_image(aa) {
  let photo = document.getElementById("img-file").files[0];
  // console.log(photo);
  let formData = new FormData();

  formData.append("file", photo);
  // fetch("http://localhost:5000/upload", {
  //   method: "POST",
  //   body: formData,
  // }).then((response) => console.log(response));
  const res = await fetch("http://localhost:5000/upload", {
    method: "POST",
    body: formData,
  });
  const data = await res.blob();
  console.log(data);
  const imgURL = URL.createObjectURL(data);
  document.querySelector("img").src = imgURL;
}
